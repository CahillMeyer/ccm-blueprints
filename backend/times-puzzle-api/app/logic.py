from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Set, Optional
import random

Pair = Tuple[int, int]

@dataclass
class TimesPlayTest:
    min_factor: int
    max_factor: int
    retry_wrong_answers: bool = False
    rng: random.Random = field(default_factory=random.Random)

    products: Dict[int, List[Pair]] = field(init=False, default_factory=dict)
    pair_usage: Dict[Pair, int] = field(init=False, default_factory=dict)
    current_pair: Optional[Pair] = field(init=False, default=None)
    current_product: Optional[int] = field(init=False, default=None)

    def __post_init__(self):
        if self.min_factor < 1 or self.max_factor < self.min_factor:
            raise ValueError('Invalid factor range')
        self._build_pairs()

    def _build_pairs(self) -> None:
        self.products.clear()
        self.pair_usage.clear()
        for a in range(self.min_factor, self.max_factor + 1):
            for b in range(a, self.max_factor + 1):  # a<=b so each pair once
                p = a * b
                self.products.setdefault(p, []).append((a, b))
        for plist in self.products.values():
            for pair in plist:
                self.pair_usage.setdefault(pair, 0)

    def set_seed(self, seed: Optional[int]) -> None:
        if seed is not None:
            self.rng.seed(seed)

    def get_product(self) -> int:
        # product chosen by the minimum usage among its factor pairs (fairness)
        prod_min = {p: min(self.pair_usage[pair] for pair in pairs)
                    for p, pairs in self.products.items()}
        min_val = min(prod_min.values())
        candidates = [p for p, v in prod_min.items() if v == min_val]
        product = self.rng.choice(candidates)
        self.current_product = product
        return product

    def random_min_used_factors(self, product: Optional[int] = None) -> Pair:
        if product is None:
            product = self.current_product
        assert product is not None, 'No product selected'
        pairs = self.products[product]
        min_use = min(self.pair_usage[p] for p in pairs)
        candidates = [p for p in pairs if self.pair_usage[p] == min_use]
        pick = self.rng.choice(candidates)
        self.current_pair = pick
        return pick

    def get_numbers(self, size: int = 9) -> List[int]:
        if size < 2:
            raise ValueError('size must be >= 2')
        product = self.get_product()
        a, b = self.random_min_used_factors(product)
        # distractor pool within factor range
        pool = list(range(self.min_factor, self.max_factor + 1))
        self.rng.shuffle(pool)
        result: Set[int] = {a, b}
        for n in pool:
            if len(result) >= size:
                break
            result.add(n)
        numbers = list(result)[:size]
        self.rng.shuffle(numbers)
        return numbers

    def check_factors(self, a: int, b: int) -> bool:
        if self.current_pair is None or self.current_product is None:
            raise RuntimeError('Round not initialized; call get_numbers first.')
        guess_pair = tuple(sorted((a, b)))
        correct = (guess_pair == self.current_pair)
        if correct or self.retry_wrong_answers:
            self.pair_usage[self.current_pair] = self.pair_usage.get(self.current_pair, 0) + 1
        return correct

    def all_numbers_used(self) -> bool:
        return all(count > 0 for count in self.pair_usage.values())

    def stats(self) -> Dict[str, int]:
        total_pairs = sum(len(pairs) for pairs in self.products.values())
        used_pairs = sum(1 for c in self.pair_usage.values() if c > 0)
        return {'total_pairs': total_pairs, 'used_pairs': used_pairs}
