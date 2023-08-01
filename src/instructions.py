from stack import Stack


def add(stack: Stack):
    a = int('0x' + str(stack.pop()), base=16)
    b = int('0x' + str(stack.pop()), base=16)
    push_(stack=stack, value=a+b)


def mul(stack: Stack):
    a = int('0x' + str(stack.pop()), base=16)
    b = int('0x' + str(stack.pop()), base=16)
    push_(stack=stack, value=a*b)


def push(stack: Stack, bytes: str, size: int):
    value = int('0x' + bytes[:size * 2], 16)
    stack.push(value=value)

def push_(stack: Stack, value: int):
    stack.push(value=value)

def push0(stack: Stack, bytes: str):
    push(stack=stack, bytes=bytes, size=0)


def push1(stack: Stack, bytes: str):
    push(stack=stack, bytes=bytes, size=1)


def sub(stack: Stack):
    a = int('0x' + str(stack.pop()), base=16)
    b = int('0x' + str(stack.pop()), base=16)
    bytes = str(a - b)
    push_(stack=stack, bytes=bytes)


class Instruction:
    def __init__(self, fn, minimumGas: int, name: str) -> None:
        self.fn = fn
        self.minimumGas = minimumGas
        self.name = name


instructions = {
    0x00: Instruction(fn=None, minimumGas=0, name="STOP"),
    0x01: Instruction(fn=add, minimumGas=3, name="ADD"),
    0x02: Instruction(fn=mul, minimumGas=5, name="MUL"),
    0x03: Instruction(fn=sub, minimumGas=3, name="SUB"),

    0x5F: Instruction(fn=push0, minimumGas=2, name="PUSH0"),
    0x60: Instruction(fn=push1, minimumGas=3, name="PUSH1")
}
