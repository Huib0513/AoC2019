#!python3
from intcodecomputer import run

startmemory = [int(i) for i in open('day19.input').read().split(",")]

grid = {0:0, 1:0}
for x in range(50):
    for y in range(50):
        memory = startmemory.copy()
        generator = run(memory, [x,y], 1)
        output = next(generator)
        #print("(" + str(x) + ", " + str(y) + ") = " + str(output[0]))
        grid[output[0]] += 1

print(grid)