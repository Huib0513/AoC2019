#!python3

line = open('day2.input').read().split(",")
instruction_pointer = 0
memory = [int(i) for i in line]
memory[1] = 12
memory[2] = 2

#Example program
#memory = [1,1,1,4,99,5,6,0,99]

while (memory[instruction_pointer] != 99):
    opcode = memory[instruction_pointer]
    parameter1 = memory[memory[instruction_pointer+1]]
    parameter2 = memory[memory[instruction_pointer+2]]
    target = memory[instruction_pointer+3]

    if opcode==1:
        print(str(parameter1) + " + " + str(parameter2) + " naar " + str(target))
        memory[target]=parameter1+parameter2
    elif opcode==2:
        print(str(parameter1) + " * " + str(parameter2) + " naar " + str(target))
        memory[target]=parameter1*parameter2
    else:
        print("Paniek, onbekende opcode")
        sys.exit()

    instruction_pointer = instruction_pointer + 4
print(memory)
