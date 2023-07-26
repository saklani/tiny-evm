# TinyEVM

We try to implement the Ethereum Virtual Machine from scratch using Python.

## What is the EVM?

A virtual machine is an emulation of a architecture. This has the advantages.
First, it makes the code hardware independent, and second, it makes code execution deterministic.
Obviously, nothing comes without trade-offs, here it is a bit of excess compute.

Ethereum as a whole can be imagined as a transaction state machine. Each transaction can be viewed as changing the world state of the Ethereum state machine. The world state can be represented as a bunch of account objects. Each account has a unique address, and is either a contract or an externally owned account (EOA).

The EVM is Ethereum's runtime environment. This means every transaction, that takes place on Ethereum, is executed on the EVM. EVM is designed to be deterministic while being able to target lots of different hardware and operating systems. Practically, the way ethereum is implemented multiple transactions are mined together to form a block.

## The Architecture

The EVM is a stack machine and therefore [https://en.wikipedia.org/wiki/Stack_machine#Comparison_with_register_machines](Turing complete). 
