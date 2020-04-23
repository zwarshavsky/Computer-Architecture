import sys

# Write a program in Python that runs programs

print(sys.argv)
program_filename = sys.argv[1]
# print(program_filename)


PRINT_BEEJ = 1 
HALT = 2 
SAVE_REG = 3 # Store a value in a register (in the LS8 called LDI)
PRINT_REG = 4 # corresponds to PRN in the LS8

memory = [0] * 256
register = [0] * 8 # like variables R0-R7, registers hold values, 
                   # they hold values at your disposal 
                   # register values persist until you change them or quit the program


# Load program into memory
address = 0 

with open(program_filename) as f:
    for line in f:
        line = line.split("#")
        line = line[0].strip()
        if line == '':
            continue
        memory[address] = int(line)
        address += 1 




pc = 0 # Program Counter, the address of the current instruction
running = True 

while running:
    inst = memory[pc]

    if inst == PRINT_BEEJ:
        print("Beej!")
        pc += 1 
    elif inst == SAVE_REG:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        pc += 3 

    elif inst == PRINT_REG:
        reg_num = memory[pc + 1]
        value = register[reg_num]
        print(value)
        pc += 2 

    elif inst == HALT:
        running = False

    else:
        print("Unknown instruction")
        running = False



