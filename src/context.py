from memory import Memory
from stack import Stack
from storage import Storage


class Context:

    def __init__(self, code: str, storage: Storage) -> None:
        self.code = code
        self.memory = Memory()
        self.program_counter = 0
        self.return_value = None
        self.run = True
        self.stack = Stack()
        self.storage = storage

    def stop(self) -> None:
        self.run = False

    def jump(self, target: int) -> None:
        self.program_counter = target

    def next(self) -> None:
        self.program_counter += 2
