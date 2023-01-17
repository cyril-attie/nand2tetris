# /usr/bin/python3

import re
from Code import Code,SYMBOL_TABLE as codeSymbolTable
from Parser import Parser
import sys

class Assembler(Parser):        
    def __init__(self, assemblyFilePath):
        self.machineLanguage = assemblyFilePath.replace('.asm','.hack')
        self.machineLines = []
        self.SYMBOL_TABLE = codeSymbolTable()
        super().__init__(assemblyFilePath)
        self.first_pass()
        self.second_pass()
        
    def first_pass(self):
        print('First pass starting')
        lineCounter = 0
        while self.hasMoreLines():
            if self.currentInstruction() == '':
                self.advance()
                continue
            elif self.instructionType() in ('C_INSTRUCTION','A_INSTRUCTION'):
                lineCounter += 1
            elif self.instructionType() == 'L_INSTRUCTION':
                self.SYMBOL_TABLE.addEntry(self.symbol(), lineCounter)
                print(f'{self.currentInstruction()}: {lineCounter+1}')
            self.advance()
        self.currentInstructionLine = 0
        print('First pass finished.')

    def second_pass(self):
        self.binaryLines = []
        print("Starting second pass!")
        while self.hasMoreLines():
            if self.currentInstruction()=='' or self.instructionType() == 'L_INSTRUCTION':
                self.advance()
                continue
            elif self.instructionType()=='C_INSTRUCTION':
                dest, comp, jump= ( Code.DEST_TABLE[self.dest()],
                                    Code.COMP_INSTRUCTIONS_TABLE[self.comp()],
                                    Code.JUMP_TABLE[self.jump()])
                machineLine = '111' + comp + dest + jump
            elif self.instructionType()=='A_INSTRUCTION':
                sym = self.symbol()
                if  self.SYMBOL_TABLE.contains(sym):
                    address = (self.SYMBOL_TABLE.getAddress(sym))
                    print(f'type of address is {type(address)} and address is {address}')
                    machineLine = Code.toBinary(address)
                elif re.findall("^[0-9]+$", sym):
                    dec=int(sym)
                    machineLine = Code.toBinary(dec)
                else:
                    address = self.SYMBOL_TABLE.newAddress()
                    print(f'newAddress is {address}')
                    self.SYMBOL_TABLE.addEntry(sym,address)
                    machineLine = Code.toBinary(address)
                    print(f'machineLine is {machineLine}')
            self.advance()
            self.binaryLines.append(machineLine)

        with open(self.machineLanguage,'w') as f:
            [print(b) for b in self.binaryLines]        
            f.write('\n'.join(self.binaryLines))
        
if __name__=='__main__':
    Assembler(sys.argv[1])
