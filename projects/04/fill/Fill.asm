// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// i=0
(LOOP0)
@i
M=0
//if RAM[KBD]!=0 goto LOOP2
(LOOP1)
@KBD
D=M
@LOOP2
D;JNE
//RAM[SCREEN+i]=0 
//if i>=8192 goto LOOP0
@SCREEN
D=A
@i
A=D+M
M=0
//i+=1
@i
M=M+1
//if i=8192 goto LOOP0
D=M
@8192
D=A-D
@LOOP0
D;JEQ
//goto LOOP1
@LOOP1
0;JMP
(LOOP2)
//if RAM[KBD]=0 goto LOOP1
@KBD
D=M
@LOOP1
D;JEQ
//RAM[SCREEN+i]=-1
@SCREEN
D=A
@i
A=D+M
M=-1
//i+=1
@i
M=M+1
//if i=8192 goto LOOP0
D=M
@8192
D=A-D
@LOOP0
D;JEQ
@LOOP2
0;JMP
	
