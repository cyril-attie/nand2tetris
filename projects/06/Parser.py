#! /usr/bin/python3

from Code import Code

class Parser(Code):
    def __init__(self,assemblyPath):
        with open(f"{assemblyPath}","r") as f:
            self.assemblyLines = f.readlines()
        self.currentInstructionLine=0
        self.binaryLines=[]
        self.outputPath = assemblyPath.strip('.asm ')+'.hack'
        [print(assemblyLine) for assemblyLine in self.assemblyLines]
        
    def currentInstruction(self):
        line = self.assemblyLines[self.currentInstructionLine].strip()
        if '//' in line and len(line.split('//'))>1 and line.split('//')[0]!='':
            currentInst = line.split('//')[0].strip()
        elif '//' in line and len(line.split('//'))>1 and line.split('//')[0]=='':
            currentInst = ''
        else: 
            currentInst = line
        print(f'Current instruction is {currentInst}')
        return currentInst

    def hasMoreLines(self):
        return len(self.assemblyLines) != self.currentInstructionLine 

    def advance(self):
        if self.hasMoreLines():
            self.currentInstructionLine += 1

    def instructionType(self):
        return self.SYMBOL_INSTRUCTION_TYPES[self.currentInstruction()[0]]

    def symbol(self):
        try:
            if self.instructionType() in self.SYMBOL_INSTRUCTION_TYPES.values():
                return self.currentInstruction().strip('@()')
            raise Exception('Not a symbol instruction')
        except Exception as e:
            print(e)

    def dest(self):
        try:
            if self.instructionType() == 'C_INSTRUCTION':
                if '=' in self.currentInstruction():
                    return self.currentInstruction().split('=')[0]
                else: return ''
            else: raise Exception('Not a C_INSTRUCTION')
        except Exception as e:
            print(e)
        return ''

    def comp(self):
        try:
            if self.instructionType() == 'C_INSTRUCTION':
                compPart = self.currentInstruction()
                if '=' in compPart: compPart = compPart.split('=')[1]
                if ';' in compPart: compPart = compPart.split(';')[0]
                return compPart
            else: raise Exception('Not a C_INSTRUCTION')
        except Exception as e:
            print(e)

    def jump(self):
        try:
            if self.instructionType() == 'C_INSTRUCTION':
                jumpPart = self.currentInstruction()
                if ';' in jumpPart: jumpPart = jumpPart.split(';')[1]
                else: jumpPart = ''
                return jumpPart
            else: raise Exception('Not a C_INSTRUCTION')
        except Exception as e:
            print(e)
        return ''
