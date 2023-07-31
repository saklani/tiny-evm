# TinyEVM

We implement the Ethereum Virtual Machine from scratch using Python.

## What is the EVM?

Simply put, EVM is Ethereum's runtime environment.
This means the execution of every smart contract instruction, that takes place on Ethereum, is executed by the EVM.
EVM is designed to be deterministic, and since its a virtual machine it can target different hardware and operating systems.

## Execution on the EVM

Smart contracts are a set of bytecode instructions for the EVM.
The smart contracts are stored in the code region of contract accounts, and are deployed by sending a transaction using an Externally Owned Account (EOA).

When the EVM executes a smart contract, a context is created for the smart contract.
The EVM context is made up of several components:

### Stack

The EVM is a stack-based machine, where each stack item has a word size of 256-bits, with maximum depth of 1024.
Each instruction is executed sequentially on the EVM, unless there is a JUMP or a JUMPI instruction.

```py
class Stack:
    def __init__(self, max_depth=1024) -> None:
        self.stack = []
        self.max_depth = max_depth

    def pop(self):
        if len(self.stack) == 0:
            raise StackUnderflow()
        self.stack.pop()

    def push(self, op: int):
        if len(self.stack) == 1024:
            raise StackOverflow()
        elif op < 0 or op > 2**256-1:
            raise InvalidOpCode()
        else:
            self.stack.push(op)
```

### Memory

The memory is a word-addressed byte array.
It is volatile which means it is destroyed once the smart contract finishes execution.

```

```