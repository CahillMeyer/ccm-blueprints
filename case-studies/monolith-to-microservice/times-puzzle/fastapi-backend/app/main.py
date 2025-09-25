from __future__ import annotations
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from uuid import uuid4
from .logic import TimesPlayTest
from . import models

app = FastAPI(title='Times Puzzle API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev-only; tighten later
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store; swap with Redis/DB if you want persistence
ROUNDS: Dict[str, TimesPlayTest] = {}

@app.post('/round', response_model=models.RoundOut)
def create_round(cfg: models.RoundCreate):
    game = TimesPlayTest(cfg.min, cfg.max, retry_wrong_answers=cfg.retry_wrong_answers)
    game.set_seed(cfg.seed)
    numbers = game.get_numbers(size=cfg.size)
    rid = str(uuid4())
    ROUNDS[rid] = game
    return {'round_id': rid, 'product': game.current_product, 'numbers': numbers}

@app.post('/guess', response_model=models.GuessOut)
def guess(payload: models.GuessIn):
    game = ROUNDS.get(payload.round_id)
    if not game:
        raise HTTPException(status_code=404, detail='Round not found')
    try:
        ok = game.check_factors(payload.a, payload.b)
        return {'correct': ok}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/status/{round_id}', response_model=models.StatusOut)
def status(round_id: str):
    game = ROUNDS.get(round_id)
    if not game:
        raise HTTPException(status_code=404, detail='Round not found')
    st = game.stats()
    return {
        'round_id': round_id,
        'all_numbers_used': game.all_numbers_used(),
        'used_pairs': st['used_pairs'],
        'total_pairs': st['total_pairs'],
    }
