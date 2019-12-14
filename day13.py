#!python3
from intcodecomputer import run

startmemory = [int(i) for i in open('day13.input').read().split(",")]

#Example program
#startmemory = [1,2,3,6,5,4]

startmemory[0] = 2
game = run(startmemory, [], 3)
total = score = paddlex = balx = 0
result = next(game)
while True:
    joystick = None
    if result[0] == -1 and result[1] == 0:
        score = result[2]
    elif result[2] == 0:
        pass
    elif result[2] == 1:
        pass
    elif result[2] == 2:
        total += 1
    elif result[2] == 3:
        paddlex = result[0]
    elif result[2] == 4:
        balx = result[0]
        if balx < paddlex:
            joystick = -1
        elif balx > paddlex:
            joystick = 1
        else:
            joystick = 0
    else:
        print("Paniek, onbekende output")
    
    try:
        result = game.send([joystick] if joystick is not None else [])
    except StopIteration:
        break

print(total)
print(score)