#!python3
from intcodecomputer import run

startmemory = [int(i) for i in open('day9.input').read().split(",")]

#Example program
#startmemory = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # Output is copy of input
#startmemory = [1102,34915192,34915192,7,4,7,99,0] # Output is 16 - digit number
#startmemory = [104,1125899906842624,99] # Output is middle number

generator = run(startmemory, [1], 1)
for result in generator:
        print(result)

generator2 = run(startmemory, [2], 1)
for result in generator2:
        print(result)