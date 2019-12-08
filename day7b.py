#!python3
import itertools

#startmemory = [int(i) for i in open('day7.input').read().split(",")]

#Example program
startmemory = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#startmemory = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def getparameter(memory, pointer, type):
    if type == 0:
        return memory[memory[pointer]]
    else:
        return memory[pointer]

def run(memory, inputs):
    ##print(memory)
    instruction_pointer = 0
    input_pointer = 0
    retval = []
    while (memory[instruction_pointer] != 99):
        #print(memory)
        opcode = "{:05d}".format(memory[instruction_pointer])[3:]
        paramtype = [int(i) for i in list("{:05d}".format(memory[instruction_pointer])[:3])]
        paramtype.reverse()

        if opcode=='01':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            memory[target]=parameter1+parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode=='02':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            memory[target]=parameter1*parameter2
            instruction_pointer = instruction_pointer + 4
        elif opcode =='03':
            # Write is *always* direct
            parameter1 = memory[instruction_pointer+1]
            # Do input
            print("Input number " + str(input_pointer) + " = " + str(inputs[input_pointer]))
            memory[parameter1] = inputs[input_pointer]
            input_pointer += 1
            instruction_pointer = instruction_pointer + 2
        elif opcode =='04':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            # Do output
            retval.append(parameter1)
            #print(parameter1)
            instruction_pointer = instruction_pointer + 2
        elif opcode=='05':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            if parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='06':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            if not parameter1:
                instruction_pointer = parameter2
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode=='07':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            memory[target]=1 if (parameter1 < parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        elif opcode=='08':
            parameter1 = getparameter(memory, instruction_pointer+1, paramtype[0])
            parameter2 = getparameter(memory, instruction_pointer+2, paramtype[1])
            target = memory[instruction_pointer+3]
            memory[target]=1 if (parameter1 == parameter2) else 0
            instruction_pointer = instruction_pointer + 4
        else:
            print("Paniek, onbekende opcode: " + opcode)
            exit()

    return retval

def run_set(phases):
    currentmemory = []
    currentmemory.append(startmemory.copy())
    currentmemory.append(startmemory.copy())
    currentmemory.append(startmemory.copy())
    currentmemory.append(startmemory.copy())
    currentmemory.append(startmemory.copy())

    input = [0]
    iteration = 0
    while True:
        print("Iteratie: "+ str(iteration))
        print([phases[0]] + input)
        iteration += 1
        input = run(currentmemory[0], [phases[0]] + input)
        #input = run(currentmemory[1], [phases[1]] + input)
        #input = run(currentmemory[2], [phases[2]] + input)
        #input = run(currentmemory[3], [phases[3]] + input)
        #input = run(currentmemory[4], [phases[4]] + input)
        if len(input) == 1:
            break

    return input


maxpower = 0
maxinput = []
for p1 in itertools.permutations(range(5,10)):
    power = run_set(p1)
    if power > maxpower:
        maxpower = power
        maxinput = p1
        #print(p1, power)
    #else:
        #print("no")
print("Maximaal vermogen " + str(maxpower) + " bereikt voor input " + str(maxinput))