from context import Context
from instructions import INSTRUCTIONS
from storage import Storage
from util import from_hex


class EVM:
    def __init__(self) -> None:
        self.storage = Storage()

    def get_instruction(self, context:  Context):
        """decodes instruction from the bytecode"""

        # Return STOP if program counter reaches end of program
        if context.program_counter >= len(code):
            return INSTRUCTIONS[0x00]

        # Extract byte from code
        opcode = from_hex(
            code[context.program_counter:  context.program_counter + 2])
        context.next()

        instruction = INSTRUCTIONS[opcode]
        return instruction

    def execute(self, code: str) -> str:
        context = Context(code=code, storage=self.storage)
        while context.run:
            instruction = self.get_instruction(context)
            instruction.fn(context)
            print(instruction.name)

        if context.return_value:
            return context.return_value


if __name__ == "__main__":
    evm = EVM()
    code = ""
    evm.execute(code)
