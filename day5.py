#!python3
startmemory = [int(i) for i in open('day5.input').read().split(",")]

#Example program
#startmemory = [1002,4,3,4,33]

opcodeparams = { 1:3, 2:3, 3:1, 4:1}
def getparameter(memory, pointer, type):
    if type == 0:
        return memory[memory[pointer]]
    else:
        return memory[pointer]

def run(memory):
    print(memory)
    instruction_pointer = 0
    while (memory[instruction_pointer] != 99):
        #print(memory)
        opcode = "{:05d}".format(memory[instruction_pointer])[3:]
        paramtype = [int(i) for i in list("{:05d}".format(memory[instruction_pointer])[:3])]
        paramtype.reverse()

        if opcode=='01':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " + " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1+parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode=='02':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " * " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1*parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode =='03':
            parameter1 = memory[instruction_pointer+1]
            #parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            print(opcode, paramtype, parameter1)
            # Do input
            memory[parameter1] = 1
            instruction_pointer = instruction_pointer + 2
        elif opcode =='04':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            print(opcode, paramtype, parameter1)
            # Do output
            print(parameter1)
            instruction_pointer = instruction_pointer + 2
        else:
            print("Paniek, onbekende opcode: " + opcode)
            exit()


    #return(memory[0])

currentmemory = startmemory.copy()
run(currentmemory)
#print(currentmemory[0])