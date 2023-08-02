from context import Context
from instructions import instructions
from storage import Storage


class EVM:
    def __init__(self) -> None:
        self.storage = Storage()

    def execute(self, code: str) -> None:
        context = Context(code=code, storage=self.storage)
        while context.run and context.program_counter < len(code):
            opcode = '0x' + \
                code[context.program_counter:  context.program_counter + 2]
            context.next()
            instruction = instructions[int(opcode, base=16)]
            instruction.fn(context)


if __name__ == "__main__":
    evm = EVM()
    code = "600660070200"
    evm.execute(code)
