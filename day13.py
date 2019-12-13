#!python3
from collections import defaultdict

start = [int(i) for i in open('day13.input').read().split(",")]

#Example program
#start = [1,2,3,6,5,4]

startmemory = defaultdict(int)
for i in range(0, len(start)):
    startmemory[i] = start[i]

def getoutputparameter(memory, pointer, type, offset):
    if type == 0:
        return memory[pointer]
    elif type == 1:
        return memory[pointer]
    else:
        return memory[pointer] + offset

def getparameter(memory, pointer, type, offset):
    if type == 0:
        return memory[memory[pointer]]
    elif type == 1:
        return memory[pointer]
    else:
        return memory[memory[pointer] + offset]

def run(memory, inputs, nrofoutputs):
    instruction_pointer = 0
    relative_base = 0
    input_pointer = 0
    outputs = []
    while (memory[instruction_pointer] != 99):
        #print(memory, instruction_pointer)
        opcode = "{:05d}".format(memory[instruction_pointer])[3:]
        paramtype = [int(i) for i in list("{:05d}".format(memory[instruction_pointer])[:3])]
        paramtype.reverse()

        if opcode=='01':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            target = getoutputparameter(memory, instruction_pointer+3, paramtype[2], relative_base)
            #target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " + " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1+parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode=='02':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            target = getoutputparameter(memory, instruction_pointer+3, paramtype[2], relative_base)
            #target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            #print(str(parameter1) + " * " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1*parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode =='03':
            parameter1 = getoutputparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            #parameter1 = memory[instruction_pointer+1]
            #print(opcode, paramtype, parameter1)
            # Do input
            #memory[parameter1] = int(input("Please provide input: "))
            memory[parameter1] = inputs[input_pointer]
            input_pointer += 1
            instruction_pointer = instruction_pointer + 2
        elif opcode =='04':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            #print(opcode, paramtype, parameter1)
            #print(opcode, parameter1, memory[parameter1])
            # Do output
            instruction_pointer = instruction_pointer + 2
            outputs.append(parameter1)
            if len(outputs) == nrofoutputs:
                yield outputs
                outputs = []
        elif opcode=='05':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            #print(opcode, paramtype, parameter1, parameter2)
            if parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='06':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            #print(opcode, paramtype, parameter1, parameter2)
            if not parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='07':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            target = getoutputparameter(memory, instruction_pointer+3, paramtype[2], relative_base)
            #target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            memory[target]=1 if (parameter1 < parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        elif opcode=='08':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1], relative_base)
            target = getoutputparameter(memory, instruction_pointer+3, paramtype[2], relative_base)
            #target = memory[instruction_pointer+3]
            #print(opcode, paramtype, parameter1, parameter2, target)
            memory[target]=1 if (parameter1 == parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        elif opcode =='09':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0], relative_base)
            #print(opcode, paramtype, parameter1)
            #Set relative_base
            relative_base += parameter1
            instruction_pointer = instruction_pointer + 2
        else:
            print("Paniek, onbekende opcode: " + opcode)
            exit()

    return

currentmemory = startmemory.copy()
game = run(currentmemory, [], 3)
screen = {}
for result in game:
    screen[(result[0], result[1])] = result[2]

print(list(screen.values()).count(2))