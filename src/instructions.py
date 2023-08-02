from context import Context
from instruction import Instruction
from util import from_hex

# Helper Functions


def __push(context: Context, size: int) -> None:
    value = context.code[context.program_counter: context.program_counter + size]
    context.stack.push(from_hex(value))
    context.next()

# Instruction Implementation


def __add__(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a+b)


def __mstore__(context: Context):
    offset = context.stack.pop()
    value = context.stack.pop()
    context.memory.store(offset, value)


def __mul__(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a*b)


def __push0__(context: Context):
    context.stack.push(value=0x0)


def __push1__(context: Context):
    __push(context, size=2)


def __push2__(context: Context):
    __push(context, size=4)


def __push3__(context: Context):
    __push(context, size=6)


def __push4__(context: Context):
    __push(context, size=8)


def __return__(context: Context):
    context.stop()
    offset = context.stack.pop()
    context.return_value = context.memory.load(offset)


def __stop__(context: Context):
    context.stop()


def __sub__(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a-b)


INSTRUCTIONS = {
    0x00: Instruction(fn=__stop__, minimumGas=0, name="STOP"),
    0x01: Instruction(fn=__add__, minimumGas=3, name="ADD"),
    0x02: Instruction(fn=__mul__, minimumGas=5, name="MUL"),
    0x03: Instruction(fn=__sub__, minimumGas=3, name="SUB"),

    0x52: Instruction(fn=__mstore__, minimumGas=3, name="MSTORE"),

    0x5F: Instruction(fn=__push0__, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=__push1__, minimumGas=3, name="PUSH1"),
    0x61: Instruction(fn=__push2__, minimumGas=3, name="PUSH2"),
    0x62: Instruction(fn=__push2__, minimumGas=3, name="PUSH3"),
    0x63: Instruction(fn=__push2__, minimumGas=3, name="PUSH4"),

    0xF3: Instruction(fn=__return__, minimumGas=0, name="RETURN")
}
