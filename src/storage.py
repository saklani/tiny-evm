class Storage:
    
    def __init__(self) -> None:
        self.storage = {}

    def load(self, key: int, value: int):
        self.storage[key] = value

    def store(self, key: int) -> int:
        return self.storage[key]