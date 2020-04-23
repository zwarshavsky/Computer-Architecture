"""CPU functionality."""

import sys

c = 6

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = [0] * 256 # RAM: starts from zero, so technically 255, pre-allocating memory 2 ** 8bit = 256 
        self.register = [0] * 8 # 
        self.LDI = 0b10000010 
        self.PRN = 0b01000111
        self.HLT = 0b00000001
        self.MUL = 0b10100010
        self.PUSH = 0b01000101
        self.POP = 0b01000110
        self.SP = 7 # power on state specifies SP as the 7th stack in our register
        self.register[self.SP] = 0xF4 # power on specifies R7 as F4 (where the stack in memory will start growing)



    def load(self,program_filename):
        """Load a program into memory."""

        # Load program into memory
        address = 0 
        with open(program_filename) as f:
            for line in f:
                line = line.split("#")
                line = line[0].strip()
                if line == '':
                    continue
                self.memory[address] = int(line,2)
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        pass
        # if op == "ADD":
        #     self.register[reg_a] += self.register[reg_b]
        # #elif op == "SUB": etc
        # else:
        #     raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.register[i], end='')

        print()

    def ram_read(self,address):
        pass

    def ram_write(self,value,address):
        pass


    def get_count(self,instruction,pc):
            inst_len = ((self.memory[pc] & instruction) >> 6) + 1   # 3
            return inst_len
    
    
    def run(self):
        """Run the CPU."""

        running = True 
        pc = 0




        while running:
            inst = self.memory[pc]
            count = self.get_count(inst,pc)

        
            if inst == self.LDI:  #Set the value of a register to an integer.
                reg_num = self.memory[pc + 1]
                value = self.memory[pc + 2]
                self.register[reg_num] = value
                pc += count 

            elif inst == self.PRN:
                reg_num = self.memory[pc + 1]
                value = self.register[reg_num]
                print(value)
                pc += count

            elif inst == self.HLT:
                running = False

            elif inst == self.MUL:
                reg_num_a = self.memory[pc + 1]
                reg_num_b = self.memory[pc + 2]
                value = self.register[reg_num_a] * self.register[reg_num_b]
                self.register[reg_num_a] = value
                pc += count

            elif inst == self.PUSH:
                # decrement the stack pointer
                self.register[self.SP] -= 1   # address_of_the_top_of_stack -= 1, 
                #                              updating the address "F4" to "F3" by updating the value stored at the R7 register   
                # copy value from register into memory
                reg_num = self.memory[pc + 1]
                value = self.register[reg_num]  # this is what we want to push
                memory_address = self.register[self.SP]
                self.memory[memory_address] = value   # store the value on the stack
                pc += count

            elif inst == self.POP:


                # value of the register is the address to the memory,
                # the value of the memory is the address to the register

                # copy value from register into memory
                memory_address = self.register[self.SP]
                value = self.memory[memory_address]


                reg_num = self.memory[pc + 1]
                self.register[reg_num] = value 
                

                # increment the stack pointer
            
                self.register[self.SP] += 1   # address_of_the_top_of_stack -= 1, 
                                              # updating the address "F4" to "F3" by updating the value stored at the R7 register
                pc += count



            else:
                print("Unknown instruction:",inst)
                running = False


if __name__ == "__main__":
    cpu = CPU()
    cpu.load("./examples/stack.ls8")
    cpu.run()
    print(cpu.memory)
    # for i in range(cpu.ram):
    #     print(cpu.ram[i])
    # 
    # print(cpu.run())
    # cpu.alu()
    # cpu.trace()