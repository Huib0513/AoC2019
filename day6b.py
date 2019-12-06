#!python3

lines = open('day6.input').read().splitlines()
#lines = [ "COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]

orbits = {}

def countorbits(center, offset):
    counter = offset * len(orbits[center]) + len(orbits[center])

    for sub in orbits[center]:
        if sub in orbits:
            counter += countorbits(sub, offset + 1)
    
    return counter

def buildpath(value):
    path = []

    for node in orbits:
        if value in orbits[node]:
            path.append(node)
            path += buildpath(node)
    return path

def findfirstcommonnode(path1, path2):
    temp = set(path2) 
    intersection = [value for value in path1 if value in temp]
    return intersection[0]

for line in lines:
    center, mass = line.split(')')
    if center in orbits.keys():
        orbits[center].append(mass)
    else:
        orbits[center]= [mass]
    #print(center,mass, orbits)

mijnpad = buildpath('YOU')
santapad = buildpath('SAN')

firstnode = findfirstcommonnode(mijnpad, santapad)

index1 = mijnpad.index(firstnode)
index2 = santapad.index(firstnode)

print(index1 + index2)