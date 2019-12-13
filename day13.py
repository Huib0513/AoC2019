#!python3
from intcodecomputer import run

startmemory = [int(i) for i in open('day13.input').read().split(",")]

#Example program
#startmemory = [1,2,3,6,5,4]

game = run(startmemory, [], 3)
screen = {}
for result in game:
    screen[(result[0], result[1])] = result[2]

print(list(screen.values()).count(2))