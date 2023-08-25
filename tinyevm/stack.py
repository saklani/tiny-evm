class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.data = []
        self.max_depth = max_depth

    def pop(self) -> int:
        if len(self.data) == 0:
            raise StackUnderflow()
        top = self.data[-1]
        self.data.pop()
        return top

    def push(self, value: int) -> None:
        if len(self.data) == 1024:
            raise StackOverflow()
        elif value < 0 or value > 2**256-1:
            raise InvalidStackValue()
        else:
            self.data.append(value)
      

# Errors

class InvalidStackValue(Exception):
    """Invalid Stack Value"""


class StackUnderflow(Exception):
    """Stack Underflow"""


class StackOverflow(Exception):
    """Stack Overflow"""
