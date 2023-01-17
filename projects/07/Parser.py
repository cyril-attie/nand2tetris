


class Parser:
    def __init__(self, inputFilePath):
        with open(inputFilePath,'r') as f:
            self.VMLines= f.readlines()
        self._currentLine = -1
        self._currentCommand = ''
        
        def hasMoreLines(self):
            return self._currentLine + 1 < len(self.VMLines)

        def advance(self):
            if not hasMoreLines():
                print('Parser.advance() was called though Parser.hasMoreLines() is false')
                raise Exception('Parser.advance() was called though Parser.hasMoreLines() is false')
            else:
                self._currentLine += 1
                self._currentCommand = self.VMLines[self._currentLine].strip().split('//')[0].strip()
                
        def commandType(self): 
            print(f'Current command is {self._currentCommand}')
            if 'add' == self._currentCommand[:3] or 'sub' == self._currentCommand[:3] or 'neg' == self._currentCommand[:3]: 
                return 'C_ARITHMETIC'
            elif 'push' == self._currentCommand[:4]:
                return 'C_PUSH'
            elif 'pop' == self._currentCommand[:3]:
                return 'C_POP'
            #To be modified with branching and function commands
            else:
                raise Exception(f'commandType could not be resolved.')

        def arg1(self):
            if self.commandType() == 'C_RETURN':
                raise Exception('arg1 method should not be called if command type is C_RETURN')
            if self.commandType() == 'C_ARITHMETIC':
                return self._currentCommand.split()[0]
            else:
                return self._currentCommand.split()[1]

        def arg2(self):
            if self.commandType() in ('C_PUSH','C_POP','C_FUNCTION','C_CALL'):
                return self._currentCommand.split()[2]



