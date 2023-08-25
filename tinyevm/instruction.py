class Instruction:
    def __init__(self, fn, minimumGas: int, name: str) -> None:
        self.fn = fn
        self.minimumGas = minimumGas
        self.name = name