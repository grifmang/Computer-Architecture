"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.halted = False

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, val):
        self.ram[address] = val

    def halt(self):
        self.halted = True

    def print_stuff(self, address):
        print(f'Value: {self.ram_read(address)}')

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc *TODO day_two?*
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
        count = 0
        while not self.halted:
            print(count)
            self.load()
            instruction = self.ram[self.pc]
            if instruction == 1:
                self.halt()
            elif instruction == 71:
                self.print_stuff(self.ram[self.pc + 1])
                self.pc += 2
            elif instruction == 130:
                self.ram_write(self.ram[self.pc + 1], self.ram[self.pc + 2])
                self.pc += 3
            else:
                print(f'unknown instruction {instruction} at address {self.pc}')
                break
            count += 1