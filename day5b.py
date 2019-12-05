#!python3
startmemory = [int(i) for i in open('day5.input').read().split(",")]

#Example program
#startmemory = [3,9,8,9,10,9,4,9,99,-1,8] # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#startmemory = [3,9,7,9,10,9,4,9,99,-1,8] # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
#startmemory = [3,3,1108,-1,8,3,4,3,99] # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#startmemory = [3,3,1107,-1,8,3,4,3,99] # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
#startmemory = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104, 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

opcodeparams = { 1:3, 2:3, 3:1, 4:1}
def getparameter(memory, pointer, type):
    if type == 0:
        return memory[memory[pointer]]
    else:
        return memory[pointer]

def run(memory):
    #print(memory)
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
            #print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " + " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1+parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode=='02':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " * " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1*parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode =='03':
            # Write is *always* direct
            parameter1 = memory[instruction_pointer+1]
            #parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            #print(opcode, paramtype, parameter1)
            # Do input
            memory[parameter1] = int(input("Please provide input: "))
            instruction_pointer = instruction_pointer + 2
        elif opcode =='04':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            #print(opcode, paramtype, parameter1)
            # Do output
            print(parameter1)
            instruction_pointer = instruction_pointer + 2
        elif opcode=='05':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            #print(opcode, paramtype, parameter1, parameter2)
            if parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='06':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            #print(opcode, paramtype, parameter1, parameter2)
            if not parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='07':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            memory[target]=1 if (parameter1 < parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        elif opcode=='08':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            memory[target]=1 if (parameter1 == parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        else:
            print("Paniek, onbekende opcode: " + opcode)
            exit()


    #return(memory[0])

currentmemory = startmemory.copy()
run(currentmemory)
#print(currentmemory[0])