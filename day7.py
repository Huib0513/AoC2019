#!python3
import itertools

startmemory = [int(i) for i in open('day7.input').read().split(",")]

#Example program
#startmemory = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#startmemory = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#startmemory = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def getparameter(memory, pointer, type):
    if type == 0:
        return memory[memory[pointer]]
    else:
        return memory[pointer]

def run(memory, inputs):
    #print(memory)
    instruction_pointer = 0
    input_pointer = 0
    retval = -1
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
            memory[parameter1] = inputs[input_pointer]
            input_pointer += 1
            instruction_pointer = instruction_pointer + 2
        elif opcode =='04':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            #print(opcode, paramtype, parameter1)
            # Do output
            retval = parameter1
            #print(parameter1)
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

    return retval

def run_set(phases):
    input = 0
    for phase in phases:
        currentmemory = startmemory.copy()
        oldinput = input
        input = run(currentmemory, [int(phase), oldinput])
    return input

maxpower = 0
maxinput = []
for p1 in itertools.permutations(range(5)):
    power = run_set(p1)
    if power > maxpower:
        maxpower = power
        maxinput = p1
        #print(p1, power)
    #else:
        #print("no")
print("Maximaal vermogen " + str(maxpower) + " bereikt voor input " + str(maxinput))