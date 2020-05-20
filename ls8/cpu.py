"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.halted = False

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, val):
        self.ram[address] = val

    def halt(self):
        self.halted = True

    def print_stuff(self, address):
        print(f'Value: {self.reg[self.ram_read(self.pc+1)]}')

    def mult(self):
        return self.alu("MUL", self.ram_read(self.pc+1), self.ram_read(self.pc+2))

    def load(self, file):
        """Load a program into memory."""

        address = 0

        with open(file) as program:
            for instruction in program:
                try:
                    instruction = int(instruction.split('#')[0][:-1], 2)
                    self.ram[address] = instruction
                    address += 1
                except:
                    continue

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == 'MUL':
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

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
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction = self.ram[self.pc]
            if instruction == 1:
                self.halt()
            elif instruction == 71:
                self.print_stuff(self.ram[self.pc + 1])
                self.pc += 2
                # self.pc += instruction >> 8
            elif instruction == 0b10000010:
                print('this is a pita')
                # self.ram_write(self.ram[self.pc + 1], self.ram[self.pc + 2])
                self.reg[self.ram_read(self.pc+1)] = self.ram_read(self.pc+2)
                self.pc += 3
                # self.pc += instruction >> 8
            elif instruction == 162:
                print(self.ram)
                print(self.reg)
                self.mult()
                self.pc += 3
            else:
                print(f'unknown instruction {instruction} at address {self.pc}')
                break