from context import Context
from instruction import Instruction
from util import calculate_twos_complement, from_hex

# Helper Functions


def __push(context: Context, size: int) -> None:
    value = context.code[context.program_counter: context.program_counter + size]
    context.stack.push(from_hex(value))
    context.jump(target=context.program_counter + size)

# Instruction Implementation


def __stop(context: Context):
    context.stop()


def __add(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a + b)


def __mul(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a * b)


def __sub(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a - b)


def __div(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a // b)


def __sdiv(context: Context):
    a = calculate_twos_complement(context.stack.pop())
    b = calculate_twos_complement(context.stack.pop())
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a // b)


def __mod(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a % b)


def __smod(context: Context):
    a = calculate_twos_complement(context.stack.pop())
    b = calculate_twos_complement(context.stack.pop())

    if b == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=a % b)


def __addmod(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    N = context.stack.pop()
    if N == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=(a + b) % N)


def __mulmod(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    N = context.stack.pop()
    if N == 0:
        context.stack.push(value=0)
    else:
        context.stack.push(value=(a * b) % N)


def __exp(context: Context):
    a = context.stack.pop()
    exponent = context.stack.pop()
    context.stack.push(value=(a ** exponent) % (2 ** 256))


def __signextend(context: Context):
    b = context.stack.pop()
    x = context.stack.pop()
    y = 0
    if b <= 31:
        t = 256 - (1 + b) * 8
    pass


def __lt(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a < b)


def __gt(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a > b)


def __slt(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a < b)


def __sgt(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a > b)


def __eq(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a == b)


def __is_zero(context: Context):
    a = context.stack.pop()
    context.stack.push(value=a == 0)


def __and(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a & b)


def __or(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a | b)


def __xor(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    context.stack.push(value=a ^ b)


def __not(context: Context):
    a = context.stack.pop()
    context.stack.push(value=~a)


def __byte(context: Context):
    i = context.stack.pop()
    x = context.stack.pop()
    y = 0
    if i <= 31:
        bin_x = bin(x)[:2][::-1]
        p = i * 8
        y = int(bin_x[p: p + 8][::-1], base=2)
    context.stack.push(value=y)


def __shl(context: Context):
    shift = context.stack.pop()
    value = context.stack.pop()
    result = 0
    if shift < 256:
        result = value << shift
    context.stack.push(value=result)


def __shr(context: Context):
    shift = context.stack.pop()
    value = context.stack.pop()
    result = 0
    if shift < 256:
        result = value >> shift
    context.stack.push(value=result)


def __mload(context: Context):
    offset = context.stack.pop()
    value = context.memory.load(offset)
    context.stack.push(value)


def __mstore(context: Context):
    offset = context.stack.pop()
    value = context.stack.pop()
    context.memory.store(offset, value)


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


INSTRUCTIONS = {
    0x00: Instruction(fn=__stop, minimumGas=0, name="STOP"),
    0x01: Instruction(fn=__add, minimumGas=3, name="ADD"),
    0x02: Instruction(fn=__mul, minimumGas=5, name="MUL"),
    0x03: Instruction(fn=__sub, minimumGas=3, name="SUB"),
    0x04: Instruction(fn=__div, minimumGas=5, name="DIV"),
    0x05: Instruction(fn=__sdiv, minimumGas=5, name="SDIV"),
    0x06: Instruction(fn=__mod, minimumGas=5, name="MOD"),
    0x07: Instruction(fn=__smod, minimumGas=5, name="SMOD"),
    0x08: Instruction(fn=__addmod, minimumGas=8, name="ADDMOD"),
    0x09: Instruction(fn=__mulmod, minimumGas=8, name="MULMOD"),
    0x0A: Instruction(fn=__exp, minimumGas=10, name="EXP"),
    0x0B: Instruction(fn=__signextend, minimumGas=5, name="SIGNEXTEND"),
    0x10: Instruction(fn=__lt, minimumGas=3, name="LT"),
    0x11: Instruction(fn=__gt, minimumGas=3, name="GT"),
    0x12: Instruction(fn=__slt, minimumGas=3, name="SLT"),
    0x13: Instruction(fn=__sgt, minimumGas=3, name="SGT"),
    0x14: Instruction(fn=__eq, minimumGas=3, name="EQ"),
    0x15: Instruction(fn=__is_zero, minimumGas=3, name="ISZERO"),
    0x16: Instruction(fn=__and, minimumGas=3, name="AND"),
    0x17: Instruction(fn=__or, minimumGas=3, name="OR"),
    0x18: Instruction(fn=__xor, minimumGas=3, name="XOR"),
    0x19: Instruction(fn=__not, minimumGas=3, name="NOT"),
    0x1A: Instruction(fn=__byte, minimumGas=3, name="BYTE"),
    0x1B: Instruction(fn=__shl,  minimumGas=3, name="SHL"),
    0x1C: Instruction(fn=__shr,  minimumGas=3, name="SHR"),


    0x51: Instruction(fn=__mload, minimumGas=5, name="MLOAD"),
    0x52: Instruction(fn=__mstore, minimumGas=3, name="MSTORE"),

    0x5F: Instruction(fn=__push0, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=__push1, minimumGas=3, name="PUSH1"),
    0x61: Instruction(fn=__push2, minimumGas=3, name="PUSH2"),
    0x62: Instruction(fn=__push3, minimumGas=3, name="PUSH3"),
    0x63: Instruction(fn=__push4, minimumGas=3, name="PUSH4"),

    0xF3: Instruction(fn=__return, minimumGas=0, name="RETURN")
}
