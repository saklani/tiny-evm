from memory import Memory
from stack import Stack
from storage import Storage


class Context:

    def __init__(self, code: str, storage: Storage) -> None:
        self.code = code
        self.memory = Memory()
        self.program_counter = 0
        self.stack = Stack()
        self.storage = storage
        self.return_value = None
        self.run = True

    def stop(self):
        self.run = False

    def jump(self, target: int):
        self.program_counter = target

    def next(self):
        self.program_counter += 2
