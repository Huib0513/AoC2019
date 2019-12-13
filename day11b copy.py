#!python3
from intcodecomputer import run
from collections import defaultdict

startmemory= [int(i) for i in open('day11.input').read().split(",")]

#Example program
#startmemory= [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # Output is copy of input
#startmemory= [1102,34915192,34915192,7,4,7,99,0] # Output is 16 - digit number
#startmemory= [104,1125899906842624,99] # Output is middle number


x = y = direction = 0
dirchange = [(0, -1), (1, 0), (0, 1), (-1, 0)]

display = defaultdict(int)
display[(x,y)] = 1
currentmemory = startmemory.copy()

generator = run(currentmemory, [display[(x,y)]], 2)
result = next(generator)
while True:
    display[(x,y)] = result[0]
    if result[1] == 0:
        direction = 3 if (direction == 0) else (direction - 1)
        x += dirchange[direction][0]
        y += dirchange[direction][1]
    else:
        direction = 0 if (direction == 3) else (direction + 1)
        x += dirchange[direction][0]
        y += dirchange[direction][1]
    
    try:
        result = generator.send([display[(x,y)]])
    except StopIteration:
        break

maxx = maxy = 0
for (x, y) in display.keys():
    if x > maxx: maxx = x
    if y > maxy: maxy = y

for row in range(maxy+1):
    line = []
    for col in range(maxx+1):
        char = ' ' if display[(col,row)] else 'X'
        line.append(char)
    print(''.join(line))
