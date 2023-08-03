from context import Context
from instruction import Instruction
from util import calculate_twos_complement, from_hex

# Helper Functions


def __push(context: Context, size: int) -> None:
    value = context.code[context.program_counter: context.program_counter + size]
    context.stack.push(from_hex(value))
    context.next()

# Instruction Implementation


def __add(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a+b)


def __div(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a//b)


def __mod(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a % b)


def __mstore(context: Context):
    offset = context.stack.pop()
    value = context.stack.pop()
    context.memory.store(offset, value)


def __mul(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a*b)


def __push0(context: Context):
    context.stack.push(value=0x0)


def __push1(context: Context):
    __push(context, size=2)


def __push2(context: Context):
    __push(context, size=4)


def __push3(context: Context):
    __push(context, size=6)


def __push4(context: Context):
    __push(context, size=8)


def __return(context: Context):
    context.stop()
    offset = context.stack.pop()
    context.return_value = context.memory.load(offset)


def __sdiv(context: Context):
    a = calculate_twos_complement(context.stack.pop())
    b = calculate_twos_complement(context.stack.pop())
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a//b)


def __smod(context: Context):
    a = calculate_twos_complement(context.stack.pop())
    b = calculate_twos_complement(context.stack.pop())

    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a % b)


def __stop(context: Context):
    context.stop()


def __sub(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a-b)


INSTRUCTIONS = {
    0x00: Instruction(fn=__stop, minimumGas=0, name="STOP"),
    0x01: Instruction(fn=__add, minimumGas=3, name="ADD"),
    0x02: Instruction(fn=__mul, minimumGas=5, name="MUL"),
    0x03: Instruction(fn=__sub, minimumGas=3, name="SUB"),
    0x04: Instruction(fn=__div, minimumGas=5, name="DIV"),
    0x05: Instruction(fn=__sdiv, minimumGas=5, name="SDIV"),
    0x06: Instruction(fn=__mod, minimumGas=5, name="MOD"),
    0x07: Instruction(fn=__smod, minimumGas=5, name="SMOD"),

    0x52: Instruction(fn=__mstore, minimumGas=3, name="MSTORE"),

    0x5F: Instruction(fn=__push0, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=__push1, minimumGas=3, name="PUSH1"),
    0x61: Instruction(fn=__push2, minimumGas=3, name="PUSH2"),
    0x62: Instruction(fn=__push3, minimumGas=3, name="PUSH3"),
    0x63: Instruction(fn=__push4, minimumGas=3, name="PUSH4"),

    0xF3: Instruction(fn=__return, minimumGas=0, name="RETURN")
}
