#!python3

startmemory = [int(i) for i in open('day2.input').read().split(",")]

#Example program
#memory = [1,1,1,4,99,5,6,0,99]

def run(memory):
    instruction_pointer = 0
    while (memory[instruction_pointer] != 99):
        opcode = memory[instruction_pointer]
        parameter1 = memory[memory[instruction_pointer+1]]
        parameter2 = memory[memory[instruction_pointer+2]]
        target = memory[instruction_pointer+3]

        if opcode==1:
            #print(str(parameter1) + " + " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1+parameter2
        elif opcode==2:
            #print(str(parameter1) + " * " + str(parameter2) + " naar " + str(target))
            memory[target]=parameter1*parameter2
        else:
            print("Paniek, onbekende opcode")
            exit()

        instruction_pointer = instruction_pointer + 4

    return(memory[0])


for noun in range(100):
    for verb in range(100):
        currentmemory = startmemory.copy()
        currentmemory[1] = noun
        currentmemory[2] = verb
        if run(currentmemory) == 19690720:
            print("noun = " + str(noun) + ", verb = " + str(verb) + ", result = " + str(noun*100 + verb) + "(" + str(currentmemory[0]) + ")")
            exit()