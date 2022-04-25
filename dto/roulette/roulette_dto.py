from dataclasses import dataclass


@dataclass(kw_only=True)
class RouletteDto:
    budget: int
    bet: int
    amount_rounds: int
