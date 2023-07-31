class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def pop(self):
        if len(self.stack) == 0:
            raise StackUnderflow()
        self.stack.pop()

    def push(self, op: int):
        if len(self.stack) == 1024:
            raise StackOverflow()
        elif op < 0 or op > 2**256-1:
            raise InvalidOpCode()
        else:
            self.stack.push(op)
      
