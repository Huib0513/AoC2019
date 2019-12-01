#!python3

lines = open('day1.input').read().splitlines()
mass = 0

for line in lines:
    mass = mass + (int(line)//3 - 2)
    print(mass)
