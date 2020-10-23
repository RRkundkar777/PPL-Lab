# About
In the previous assignment, we had a brief introduction on ELF Structure

But we mainly explored the .text section of elf which contains OPCODES for Assembly instructions.

In this Assignment, we will explore the stack section of ELF and study the memory layout of C programs

## Commands used
```
gcc -gstabs source.c -o src
gdb src
```

## GDB Commands used
```
run
break main
break function
break main+N
nexti / ni
next
```
## The Stack Section

The stack section contains function parameters, local variables and a return address.

Basically, a stack stores all the essential data of function call.

In this assignment we studied how this data is stored inside a stack. What is memory layout of C programs.

We constructed a memory layout diagram for the same.

## Buffer Overflow Attack

As a part of understanding the Memory Layout of C  programs and the Stack, we implemented a program which skips the instruction "X = 1" by modifying the return address of a function.











