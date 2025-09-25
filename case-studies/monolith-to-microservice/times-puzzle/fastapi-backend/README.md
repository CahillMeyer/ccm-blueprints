# Times Puzzle API (FastAPI)

A small REST API that serves "multiplication puzzle" rounds.
It mirrors the fairness logic from a UE C++ prototype: pick a product whose
factor pairs are **least used**, choose one pair, return a shuffled set of
numbers (two correct, the rest distractors), and validate guesses.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://localhost:8000/docs
```
## Endpoints

- POST /round – body: {min, max, size, retry_wrong_answers?, seed?} → {round_id, product, numbers}

- POST /guess – body: {round_id, a, b} → {correct}

- GET /status/{round_id} → {all_numbers_used, used_pairs, total_pairs}

### Notes

- State is in-memory for simplicity; swap with Redis/Postgres if needed.

- Fairness mirrors the C++ grouping by product and least-used pair.


