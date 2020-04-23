#THIS IS A SHIFT

This is analogous to bitwise, but using base10, not hex

Decimal
  vv
123456


want 34 from the above number

003400 #this is not the number yet
000340
000034 #this is the number

Lesson: requires multiple separate operations 
to succesfully isolate the number you need


mask - to extract specific number
shifting - turn off bits individually - EXPLAIN SHIFT TO YOURSELF AGAIN



Instructions

operand is an argument to the opp code

e.g. 10101000 000000aaa 00000000bbb

first - the operation
second - first number
third - third number 

In the second and third, the aaa and bbb represent registered numbers, 
e.g. a vs b when performing operation requiring two register arguments. 
The 3 bits "aaa" represent that SPECIFIC register. It is not a relative reference.  


Terms

ALU - arithmetical logic unit, math, arithmetic, or logic. For instance, CALL is not


Figuring out length of instruction lines

LDI 10000

LDI R2,37

pc += 3 


extracing number of operands 

  10000010
& 11000000

-----------

1000000
0100000
....
0000010

inst_len = (ir & ob1100000) >> 6) + 1  #look at the number of operands + 1 
to see how many lines you have to jump

100000010
000000010
00100101 #37
00000000 # NOP
00000000 # NOP
00000000 # NOP


AND - clear bits to 0, mask out bits
OR: set bits to 1
SHIFT: with AND - extract individual sets of bits

**MOST OPERANDS YOU CAN HAVE IS 3**


Day 2: Multiply instruction 


