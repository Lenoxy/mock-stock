class Stock():
    def __init__(self) -> None:
        self.id: str = None
        self.value: float = None
        self.history: dict = None
        self.name: str = None
        self.change: float = None
        self.amount: int = None


    def to_json(self) -> dict:
        return {'id': self.id,
            'value': self.value,
            'name': self.name,
            'change': self.change,
            'history': self.history,
            'amount': self.amount,}
