#!python3

#lines = open('day6.input').read().splitlines()
lines = [ "COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]

orbits = {}

def countorbits(center, offset):
    counter = offset * len(orbits[center]) + len(orbits[center])

    for sub in orbits[center]:
        if sub in orbits:
            counter += countorbits(sub, offset + 1)
    
    return counter


for line in lines:
    center, mass = line.split(')')
    if center in orbits.keys():
        orbits[center].append(mass)
    else:
        orbits[center]= [mass]
    #print(center,mass, orbits)

print(countorbits('COM', 0))