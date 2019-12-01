#!python3

lines = open('day1.input').read().splitlines()
mass = 0

def calculateFuel(mass):
    fuel = (mass//3 - 2)
    if fuel < 0:
        fuel = 0

    if fuel > 0:
        fuel = fuel + calculateFuel(fuel)
    return fuel

for line in lines:
    mass = mass + (calculateFuel(int(line)))
    print(mass)
