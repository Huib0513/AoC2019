#!python3
from intcodecomputer import run

startmemory = [int(i) for i in open('day19.input').read().split(",")]

x = startx = 0
y = starty = 99

while True:
    y+=1
    #print('Checking row ' + str(y))
    # Find first affected cell on current row
    while True:
        generator = run(startmemory, [x,y], 1)
        output = next(generator)
        if output[0]:
            startx = x
            #print("First affected x is " + str(x) + "(" + str(output) + ")")
            break
        x += 1

    # Check right top corner
    #print("Checking (" + str(startx + 100) + ", "+ str(y - 100)+ ")")
    generator = run(startmemory, [startx + 99,y-99], 1)
    output = next(generator)
    if not output[0]:
        continue
    # Check right bottom corner
    #print("Checking (" + str(startx + 100) + ", "+ str(y) + ")")
    generator = run(startmemory, [startx + 99,y], 1)
    output = next(generator)
    if not output[0]:
        continue
    # Check left top corner
    #print("Checking (" + str(startx) + ", "+ str(y - 100) + ")")
    generator = run(startmemory, [startx,y - 99], 1)
    output = next(generator)
    if not output[0]:
        continue
    print("First usable cell is at (" + str(startx) + ", " + str(y - 99)+")" )
    break
