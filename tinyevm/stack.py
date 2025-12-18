class Stack:
    def __init__(self, max_depth: int = 1024) -> None:
        self.data: list[int] = []
        self.max_depth = max_depth

    def pop(self) -> int:
        if not self.data:
            raise StackUnderflow()
        return self.data.pop()

    def push(self, value: int) -> None:
        if len(self.data) >= self.max_depth:
            raise StackOverflow()
        if not (0 <= value <= 2**256 - 1):
            raise InvalidStackValue()
        self.data.append(value)

    def peek(self, n: int = 0) -> int:
        """Look at nth item from top (0 = top)."""
        if n >= len(self.data):
            raise StackUnderflow()
        return self.data[-(n + 1)]

    def swap(self, n: int) -> None:
        """Swap top with nth item below it (n >= 1)."""
        if n >= len(self.data):
            raise StackUnderflow()
        self.data[-1], self.data[-(n + 1)] = self.data[-(n + 1)], self.data[-1]

    def duplicate(self, n: int) -> None:
        """Duplicate nth item from top to top (n >= 1)."""
        if n > len(self.data):
            raise StackUnderflow()
        self.push(self.data[-n])

    def __len__(self) -> int:
        return len(self.data)


# Errors

class InvalidStackValue(Exception):
    """Invalid Stack Value"""


class StackUnderflow(Exception):
    """Stack Underflow"""


class StackOverflow(Exception):
    """Stack Overflow"""
