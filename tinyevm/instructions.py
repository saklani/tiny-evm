from tinyevm.context import Context
from tinyevm.instruction import Instruction
from tinyevm.utils import calculate_twos_complement, from_hex

# Helpers
UINT_MAX = 2 ** 256 - 1
UINT_MIN = 0


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
    if a + b > UINT_MAX:
        value = (a + b) - UINT_MAX - 1
    else:
        value = a + b
    context.stack.push(value)


def __mul(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if a * b > UINT_MAX:
        value = (a * b) - UINT_MAX - 1
    else:
        value = a * b
    context.stack.push(value)


def __sub(context: Context):
    a = context.stack.pop()
    b = context.stack.pop()
    if a - b < UINT_MIN:
        value = UINT_MAX + (a - b) + 1
    else:
        value = a - b
    context.stack.push(value)


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


def __sar(context: Context):
    pass


def __sha3(context: Context):
    offset = context.stack.pop()
    size = context.stack.pop()
    if size > 31:
        return 0
    result = context.memory.load(offset, size)


def __pop(context: Context):
    context.stack.pop()


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


def __push5(context: Context):
    __push(context, size=10)


def __push6(context: Context):
    __push(context, size=12)


def __push7(context: Context):
    __push(context, size=14)


def __push8(context: Context):
    __push(context, size=16)


def __push9(context: Context):
    __push(context, size=18)


def __push10(context: Context):
    __push(context, size=20)


def __push11(context: Context):
    __push(context, size=22)


def __push12(context: Context):
    __push(context, size=24)


def __push13(context: Context):
    __push(context, size=26)


def __push14(context: Context):
    __push(context, size=28)


def __push15(context: Context):
    __push(context, size=30)


def __push16(context: Context):
    __push(context, size=32)


def __push17(context: Context):
    __push(context, size=34)


def __push18(context: Context):
    __push(context, size=36)


def __push19(context: Context):
    __push(context, size=38)


def __push20(context: Context):
    __push(context, size=40)


def __push21(context: Context):
    __push(context, size=42)


def __push22(context: Context):
    __push(context, size=44)


def __push23(context: Context):
    __push(context, size=46)


def __push24(context: Context):
    __push(context, size=48)


def __push25(context: Context):
    __push(context, size=50)


def __push26(context: Context):
    __push(context, size=52)


def __push27(context: Context):
    __push(context, size=54)


def __push28(context: Context):
    __push(context, size=56)


def __push29(context: Context):
    __push(context, size=58)


def __push30(context: Context):
    __push(context, size=60)


def __push31(context: Context):
    __push(context, size=62)


def __push32(context: Context):
    __push(context, size=64)


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
    0x1D: Instruction(fn=__sar,  minimumGas=3, name="SAR"),
    0x1E: Instruction(fn=__sha3,  minimumGas=30, name="SHA3"),

    0x50: Instruction(fn=__pop, minimumGas=2, name="POP"),
    0x51: Instruction(fn=__mload, minimumGas=5, name="MLOAD"),
    0x52: Instruction(fn=__mstore, minimumGas=3, name="MSTORE"),

    0x5F: Instruction(fn=__push0, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=__push1, minimumGas=3, name="PUSH1"),
    0x61: Instruction(fn=__push2, minimumGas=3, name="PUSH2"),
    0x62: Instruction(fn=__push3, minimumGas=3, name="PUSH3"),
    0x63: Instruction(fn=__push4, minimumGas=3, name="PUSH4"),
    0x64: Instruction(fn=__push5, minimumGas=3, name="PUSH5"),
    0x65: Instruction(fn=__push6, minimumGas=3, name="PUSH6"),
    0x66: Instruction(fn=__push7, minimumGas=3, name="PUSH7"),
    0x67: Instruction(fn=__push8, minimumGas=2, name="PUSH8"),
    0x68: Instruction(fn=__push9, minimumGas=3, name="PUSH9"),
    0x69: Instruction(fn=__push10, minimumGas=3, name="PUSH10"),
    0x6A: Instruction(fn=__push11, minimumGas=3, name="PUSH11"),
    0x6B: Instruction(fn=__push12, minimumGas=3, name="PUSH12"),
    0x6C: Instruction(fn=__push13, minimumGas=3, name="PUSH13"),
    0x6D: Instruction(fn=__push14, minimumGas=3, name="PUSH14"),
    0x6E: Instruction(fn=__push15, minimumGas=3, name="PUSH15"),
    0x6F: Instruction(fn=__push16, minimumGas=2, name="PUSH16"),
    0x70: Instruction(fn=__push17, minimumGas=3, name="PUSH17"),
    0x71: Instruction(fn=__push18, minimumGas=3, name="PUSH18"),
    0x72: Instruction(fn=__push19, minimumGas=3, name="PUSH19"),
    0x73: Instruction(fn=__push20, minimumGas=3, name="PUSH20"),
    0x74: Instruction(fn=__push21, minimumGas=3, name="PUSH21"),
    0x75: Instruction(fn=__push22, minimumGas=3, name="PUSH22"),
    0x77: Instruction(fn=__push23, minimumGas=3, name="PUSH23"),
    0x77: Instruction(fn=__push24, minimumGas=2, name="PUSH24"),
    0x78: Instruction(fn=__push25, minimumGas=3, name="PUSH25"),
    0x79: Instruction(fn=__push26, minimumGas=3, name="PUSH26"),
    0x7A: Instruction(fn=__push27, minimumGas=3, name="PUSH27"),
    0x7B: Instruction(fn=__push28, minimumGas=3, name="PUSH28"),
    0x7C: Instruction(fn=__push29, minimumGas=3, name="PUSH29"),
    0x7D: Instruction(fn=__push30, minimumGas=3, name="PUSH30"),
    0x7E: Instruction(fn=__push31, minimumGas=3, name="PUSH31"),
    0x7F: Instruction(fn=__push32, minimumGas=3, name="PUSH32"),


    0xF3: Instruction(fn=__return, minimumGas=0, name="RETURN")
}
