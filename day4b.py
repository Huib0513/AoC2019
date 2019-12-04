#!python3

lines = open('day4.input').read().splitlines()
number = 0

def isvalidpwd(number):
    valid = 0
    temp = str(number)

    for letter in range(0, len(temp)-1):
        if (int(temp[letter]) > int(temp[letter+1])):
            # Number is not ascending
            return False
        if temp.count(temp[letter]) == 2:
                valid = 1
    return valid

start, stop = int(lines[0].split('-')[0]), int(lines[0].split('-')[1])
for counter in range(start,stop):
    if isvalidpwd(counter):
        #print(counter)
        number += 1

print("And the number is: " + str(number))