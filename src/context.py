from instructions import instructions
from memory import Memory
from stack import Stack
from storage import Storage


class Context:
    """Execution context"""

    def __init__(self) -> None:
        self.memory = Memory()
        self.stack = Stack()
        self.storage = Storage()
        self.run = True
        self.program_counter = 0

    def execute(self, code: str):
        while self.run and self.program_counter < len(code):
            opcode = '0x' + \
                code[self.program_counter:  self.program_counter + 2]
            self.program_counter += 2
            print(self.stack.stack, opcode)
            instruction = instructions[int(opcode, base=16)]
            if (instruction.name == "STOP"):
                self.halt()
            elif instruction.name == "PUSH1":
                instruction.fn(stack=self.stack,
                               bytes=code[self.program_counter:])
                self.program_counter += 2
            else:
                instruction.fn(stack=self.stack)

    def halt(self):
        self.run = False


if __name__ == "__main__":
    evm = Context()
    code = "600660070200"
    evm.execute(code)
