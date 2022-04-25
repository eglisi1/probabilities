from dataclasses import dataclass
from decimal import Decimal


@dataclass(kw_only=True)
class BirthdayDto:
    amount_people: int
    probability: Decimal
