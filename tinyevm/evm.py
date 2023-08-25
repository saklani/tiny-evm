from tinyevm.context import Context
from tinyevm.instruction import Instruction
from tinyevm.instructions import INSTRUCTIONS
from tinyevm.storage import Storage
from tinyevm.utils import from_hex


class EVM:
    def __init__(self) -> None:
        self.context = None
        self.storage = Storage()

    def get_instruction(self, context:  Context) -> Instruction:
        """decodes instruction from the bytecode"""

        # Return STOP if program counter reaches end of program
        if context.program_counter >= len(context.code):
            return INSTRUCTIONS[0x00]

        # Extract byte from code
        opcode = from_hex(
            context.code[context.program_counter:  context.program_counter + 2])
        context.next()

        instruction = INSTRUCTIONS[opcode]
        return instruction

    def execute(self, code: str) -> str:
        self.context = Context(code=code, storage=self.storage)
        while self.context.run:
            instruction = self.get_instruction(self.context)
            instruction.fn(self.context)
        if self.context.return_value:
            return self.context.return_value
        return ""
