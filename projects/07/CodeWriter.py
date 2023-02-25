

class CodeWriter:
    def __init__(self, filePath):
        self.f = open(filePath,'w')
        self.comparisonCounter=0

    def writeArithmetic(self, command):
        if command in ('eq','gt','lt'):
            self.comparisonCounter += 1
        helperArithmetic2Args = lambda operationTemplate: '@SP\nA=M-1\nD=M\nA=A-1\n{operationTemplate}M=D\n@SP\nM=M-1'
        commandTemplateFor = {
                'add': helperArithmetic2Args(f'D=D+M\n'),
                'sub': helperArithmetic2Args(f'D=D-M\n'),
                'eq': f'D=D-M\nM=0\nD;JNE\n(FALSE)\n',
                'gt': f'D=D+M\n',
                'lt': f'',
                'and': helperArithmetic2Args(f'D=D&M\n'),
                'or': helperArithmetic2Args(f'D=D|M\n'),
                'not': f'@SP\nA=M-1\nM=!M\n',
                'neg': f'@SP\nA=M-1\nM=-M\n',
                }
        assemblyResult = f'''
        //{command}
        {commandTemtplateFor[command]}
        '''

    def writePushPop(self, command, segment, index):
        assemblyResult = f'\n\n//{command} {segment} {index}\n' 

        if command == 'C_PUSH':
            helperPushArgLclThisThat = lambda segmentRegisterName : f'@{segmentRegisterName}\nD=M\n@{index}\nA=D+A\nD=M\n'
            pushSegmentTemplateFor = {
                'constant'  : f'@{index}\nD=A',
                'argument'  : helperPushArgLclThisThat('ARG'), 
                'local'     : helperPushArgLclThisThat('LCL'),
                'this'      : helperPushArgLclThisThat('THIS'), 
                'that'      : helperPushArgLclThisThat('THAT'), 
                'static'    : f'@static{index}\nD=M}',
                'pointer'   : f'@{3+index}\nD=M\n'
                'temp'      : f'@{5+index}\nD=M\n'
                }

            assemblyResult += f'''
            {pushSegmentTemplateFor[segment]}
            @SP
            A=M
            M=D
            @SP
            M=M+1  
            '''

        elif command== 'C_POP':
            helperPopArgLclThisThat = lambda segmentRegisterName : f'@{segmentRegisterName}\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n'
            popSegmentTemplateFor = {
                'argument'  : helperPopArgLclThisThat('ARG'), 
                'local'     : helperPopArgLclThisThat('LCL'),
                'this'      : helperPopArgLclThisThat('THIS'), 
                'that'      : helperPopArgLclThisThat('THAT'), 
                'static'    : f'@static{index}\nD=A\n@R13\nM=D\n',
                'pointer'   : f'@{3+index}\nD=A\n@R13\nM=D\n'
                'temp'      : f'@{5+index}\nD=A\n@R13\nM=D\n'
                    }
            assemblyResult += f'''
            {popSegmentTemplateFor[segment]}
            @SP
            A=M-1
            D=M
            @R13
            A=M
            M=D
            @SP
            M=M-1
            '''

        else: 
            raise Exception('Command is neither push nor pop! Cannot execute writePushPop')

        self.f.write(assemblyResult)
        

    def close(self):
        self._writeInfiniteLoop()
        self.f.close()

    def _writeInfiniteLoop(self):
        s = '''
        (END)
        @END
        0;JMP
        '''
        self.f.write(s)
