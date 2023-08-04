class Memory:

    def __init__(self):
        self.memory = []

    def load(self, offset: int):
        if offset < 0:
            raise MemoryOffsetUnderflow()

        if offset >= self.size():
            return 0

        return self.memory[offset]

    def store(self, offset: int, value: int):
        if offset < 0:
            raise MemoryOffsetUnderflow()

        if value < 0 or value > 2 ** 256 - 1:
            raise InvalidMemoryValue()

        offset //= 32

        # Memory increments in multiples of 32 bytes (256 bits)
        # each value is 32 bytes
        # So, if offset = 0...31 the value at 0 is overwritten,
        # similarly if offset = 32...63 the value 1 is overwritten, and so on.
        if offset >= len(self.memory):
            self.memory.extend([0] * (offset - len(self.memory) + 1))
        self.memory[offset] = value

    def size(self) -> int:
        return len(self.memory) * 32


class InvalidMemoryValue(Exception):
    """Invalid memory value"""


class MemoryOffsetOverflow(Exception):
    """Memory offset overflow"""


class MemoryOffsetUnderflow(Exception):
    """Memory offset underflow"""
