# Assembler
this is where we'll aupload all our codes
This repository contains assembler code to convert assembly into machine code with the following specifications:


Instructions
The instructions supported are:

Arithmetic:
add: Add two registers and store in third register.
sub: Subtract two registers and store in third register.
Move:
mov1 (immediate to register): Move immediate value to register.
mov2 (register to register): Move value from one register to another.
Load/Store:
ld: Load value from memory address in register.
st: Store register value in memory.
Multiply/Divide:
mul: Multiply two registers and store in third register.
div: Divide two registers and store in third register.
Shift:
ls: Logical left shift. Shift left by immediate places.
rs: Logical right shift. Shift right by immediate places.
Logical:
xor: Exclusive OR two registers and store in third register.
or: OR two registers and store in third register.
and: AND two registers and store in third register.
Compare:
cmp: Compare two registers. Set flags in FLAGS register.
Unconditional Jump:
jmp: Jump to label.
Conditional Jumps:
jlt: Jump to label if less than (signed).
jgt: Jump to label if greater than (signed).
je: Jump to label if equal.
Halt:
hlt: Halt program.
Registers
The registers are R0 to R7. R7 is used as the FLAGS register to store the flags from the cmp instruction.

Variables
Variables need to be defined at the start of the program using the var directive. For example:

Copy
var x 
var y
Variables are stored in memory with the address incrementing by 1 for each variable.

Labels
Labels can be defined using label_name: and used in jump instructions. For example:

Copy
loop: 
jmp loop
The labels dictionary keeps tracks of the addresses of each label defined.

Structure
The assembly code needs to follow this structure:

Variable definitions
Instructions
hlt instruction
Errors
The code checks for the following errors:

Typos in instructions
Use of undefined variables
Use of undefined labels
Illegal use of FLAGS register
Immediate values greater than 8 bits
Label defined as variable or vice versa
Missing hlt instruction
Last line not hlt
General syntax errors
Program flow
The program reads each line of assembly code and generates the 16-bit machine code. It also keeps track of the program counter and updates the labels dictionary with the address for each label.
