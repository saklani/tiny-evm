class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def pop(self) -> int:
        if len(self.stack) == 0:
            raise StackUnderflow()
        top = self.stack[-1]
        self.stack.pop()
        return top

    def push(self, value: int) -> None:
        if len(self.stack) == 1024:
            raise StackOverflow()
        elif value < 0 or value > 2**256-1:
            raise InvalidStackValue()
        else:
            self.stack.append(value)
      

# Errors

class InvalidStackValue(Exception):
    """Invalid Stack Value"""


class StackUnderflow(Exception):
    """Stack Underflow"""


class StackOverflow(Exception):
    """Stack Overflow"""
