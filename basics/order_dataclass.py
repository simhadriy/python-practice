from dataclasses import dataclass,field

@dataclass(frozen=True)
class Order:
    id: str
    amount: float
    tags: list[str] = field(default_factory=list)

orders = [
    Order("a1", 30.0),
    Order("b2", 10.0, ["rush"]),
    Order("c3", 20.0, ["gift", "rush"]),
]

by_amount = sorted(orders, key=lambda o: o.amount)

print(by_amount)