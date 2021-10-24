class Stock():
    def __init__(self) -> None:
        self.id: str
        self.value: float
        self.history: dict = None
        self.name: str
        self.change: float


    def to_json(self) -> dict:
        if self.history:
            return {'id': self.id,
                'value': self.value,
                'name': self.name,
                'change': self.change,
                'history': self.history,}

        return {'id': self.id,
                'value': self.value,
                'name': self.name,
                'change': self.change,}
