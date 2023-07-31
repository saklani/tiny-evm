from error import InvalidStackValue, StackOverflow, StackUnderflow


class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def pop(self):
        if len(self.stack) == 0:
            raise StackUnderflow()
        self.stack.pop()

    def push(self, value: int):
        if len(self.stack) == 1024:
            raise StackOverflow()
        elif value < 0 or value > 2**256-1:
            raise InvalidStackValue()
        else:
            self.stack.push(value)
      
