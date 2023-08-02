from context import Context
from instruction import Instruction


# Helper

def to_hex(value: int) -> int:
    return int('0x' + str(value), base=16)

def push(context: Context, size: int) -> None:
    value = context.code[context.program_counter: context.program_counter + size]
    context.stack.push(int('0x' + value, base=16))
    context.next()


# Instruction Implementation

def add(context: Context):
    a = to_hex(context.stack.pop())
    b = to_hex(context.stack.pop())
    context.stack.push(value=a+b)


def mul(context: Context):
    a = to_hex(context.stack.pop())
    b = to_hex(context.stack.pop())
    context.stack.push(value=a*b)


def push0(context: Context):
    context.stack.push(value=0x0)


def push1(context: Context):
    push(context, size=2)


def push2(context: Context):
    push(context, size=4)


def stop(context: Context):
    context.halt()


def sub(context: Context):
    a = to_hex(context.stack.pop())
    b = to_hex(context.stack.pop())
    context.stack.push(value=a-b)


instructions = {
    0x00: Instruction(fn=stop, minimumGas=0, name="STOP"),
    0x01: Instruction(fn=add, minimumGas=3, name="ADD"),
    0x02: Instruction(fn=mul, minimumGas=5, name="MUL"),
    0x03: Instruction(fn=sub, minimumGas=3, name="SUB"),

    0x5F: Instruction(fn=push0, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=push1, minimumGas=3, name="PUSH1")
}
