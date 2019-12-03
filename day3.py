#!python3

lines = open('day3.input').read().splitlines()
#lines = ['R8,U5,L5,D3', 'U7,R6,D4,L4']

def addpoints(route, start, steps):
    currentx = start[0]
    currenty = start[1]

    if steps[0] == 'R':
        for _ in range(int(steps[1:])):
            currentx = currentx + 1
            route.append((currentx, currenty))
    elif steps[0] == 'L':
        for _ in range(int(steps[1:])):
            currentx = currentx - 1
            route.append((currentx, currenty))
    elif steps[0] == 'U':
        for _ in range(int(steps[1:])):
            currenty = currenty + 1
            route.append((currentx, currenty))
    elif steps[0] == 'D':
        for _ in range(int(steps[1:])):
            currenty = currenty - 1
            route.append((currentx, currenty))

def intersection(lst1, lst2): 
    # Easy and *very* slow intersection:
    # lst3 = [value for value in lst1 if value in lst2] 

    # Use set to speed up intersection: set *will* remove duplicate entries, but that is not a problem in this case
    temp = set(lst2) 
    lst3 = [value for value in lst1 if value in temp] 
    return lst3 

wire = []
currentline = 0
for line in lines:
    wire.append([(0,0)])
    for segment in line.split(','):
        addpoints(wire[currentline], wire[currentline][-1], segment)
    currentline = currentline + 1

commonpoints = intersection(wire[0][1:], wire[1][1:])
print(commonpoints)
distances = [abs(item[0])+abs(item[1]) for item in commonpoints]
print(distances)

print("The nearest crossing is at distance: " + str(min(distances)))
