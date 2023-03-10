from collections import defaultdict

class SYMBOL_TABLE:
    PREDEFINED_SYMBOLS= (
        ('SP',          0),
        ('LCL',         1),
        ('ARG',         2),
        ('THIS',        3),
        ('THAT',        4),
        ('SCREEN',      16384),
        ('KBD',         24576),
		('R0',			0),
		('R1',			1),
		('R2',			2),
		('R3',			3),
		('R4',			4),
		('R5',			5),
		('R6',			6),
		('R7',			7),
		('R8',			8),
		('R9',			9),
		('R10',			10),
		('R11',			11),
		('R12',			12),
		('R13',			13),
		('R14',			14),
		('R15',			15)
            )

    def __init__(self):
        self._table= {}
        self.addEntry = lambda a,v: self._table.update({a: v})
        self.contains = lambda x : (x in self._table.keys())
        self.getAddress = lambda a : self._table[a]
        [self.addEntry(predefined_symbol[0], predefined_symbol[1]) for predefined_symbol in self.PREDEFINED_SYMBOLS]
        self.base,self.providedAddresses = 15,0
    
    def newAddress(self):
        self.providedAddresses+=1
        return self.base + self.providedAddresses
    

class Code:
    SYMBOL_INSTRUCTION_TYPES = defaultdict(lambda:'C_INSTRUCTION',{'@':'A_INSTRUCTION', '(':'L_INSTRUCTION'})

    COMP_INSTRUCTIONS_TABLE = {
                '0'     :'0101010',
                '1'     :'0111111',
                '-1'    :'0111010',
                'D'     :'0001100',
                'A'     :'0110000',
                'M'     :'1110000',
                '!D'    :'0001101',
                '!A'    :'0110001',
                '!M'    :'1110001',
                '-D'    :'0001111',
                '-A'    :'0010011',
                '-M'    :'1010011',
                'D+1'   :'0011111',
                'A+1'   :'0110111',
                'M+1'   :'1110111',
                'D-1'   :'0001110',
                'A-1'   :'0110010',
                'M-1'   :'1110010',
                'D+A'   :'0000010',
                'D+M'   :'1000010',
                'D-A'   :'0010011',
                'D-M'   :'1010011',
                'A-D'   :'0000111',
                'M-D'   :'1000111',
                'D&A'   :'0000000',
                'D&M'   :'1000000',
                'D|A'   :'0010101',
                'D|M'   :'1010101'
            }

    JUMP_TABLE = {
                '':'000',
                'JGT':'001',
                'JEQ':'010',
                'JGE':'011',
                'JLT':'100',
                'JNE':'101',
                'JLE':'110',
                'JMP':'111'
            }
 
    DEST_TABLE ={    'A'     :'100',
                                        'AD'    :'110',
                                        'AMD'   :'111',
                                        'D'     :'010',
                                        'MD'    :'011',
                                        'M'     :'001',
                                        'AM'    :'101',
                                        ''      :'000'
                                        } 

    toBinary = lambda x: bin(x).replace('0b','').zfill(16)
