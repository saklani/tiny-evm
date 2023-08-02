from context import Context
from instructions import instructions
from storage import Storage
from util import from_hex


class EVM:
    def __init__(self) -> None:
        self.storage = Storage()

    def execute(self, code: str) -> str:
        context = Context(code=code, storage=self.storage)
        while context.run and context.program_counter < len(code):
            opcode = from_hex(code[context.program_counter:  context.program_counter + 2])
            context.next()
            instruction = instructions[opcode]
            instruction.fn(context)
            
        if context.return_value:
           return context.return_value


if __name__ == "__main__":
    evm = EVM()
    code = "604260005260206000F3"
    print(evm.execute(code))
