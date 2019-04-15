#Members do not need a mate to reproduce

# NEEDED

import random

#input to guess

number = int(input("ENTER NUMBER 1-10: "))

#defining society

population = 3

global generation
generation = 0

generation = 0

mem1 = random.randint(1, 10)

mem2 = random.randint(1, 10)

mem3 = random.randint(1, 10)

NotGoal = 1

#loop to countinue till goal is reached

#fitness
'''-----------------------------------------'''


    
def create_child_plus_fitness():

    global generation
    global mem1
    global mem2
    global mem3
    
    generation += 1
    
    print(generation)
    
    print(mem1)

    print(mem2)

    print(mem3)

#getting fitness data
    if (mem1 > number):
        mem1 = mem1 - number

    if (mem2 > number):
        mem2 = mem1 - number

    if (mem3 > number):
        mem3 = mem3 - number


    if (mem1 < number):
        mem1 = number - mem1


    if (mem2 < number):
        mem2 = number - mem2

    if (mem3 < number):
        mem3 = number - mem3
#sorting data

    fitness_amounts = [mem1, mem2, mem3]

    fitness_amounts.sort()



    

    mem1 = fitness_amounts[1]

    mem1_mutate = random.randint(1, 3)

    mem2 = fitness_amounts[1]

    mem2_mutate = random.randint(1, 3)

    mem3 = fitness_amounts[1]

    mem3_mutate = random.randint(1, 3)

    if (mem1_mutate == 1):
        mem1 = mem1 + 0

    if (mem1_mutate == 2):
        mem1 = mem1 + 1

    if (mem1_mutate == 3):
        mem1 = mem1 - 0


    if (mem2_mutate == 1):
        mem2 = mem2 + 0

    if (mem2_mutate == 2):
        mem2 = mem2 + 1

    if (mem2_mutate == 3):
        mem2 = mem2 - 0



    if (mem3_mutate == 1):
        mem3 = mem3 + 0

    if (mem3_mutate == 2):
        mem3 = mem3 + 1

    if (mem3_mutate == 3):
        mem3 = mem3 - 0
'''------------------------------------------------------------------------'''        
def goal_reached():

# We but the member number so we can know who did it

    if (mem1 == number):
        print('member1:',"The number is", mem1)
        exit()
        

    if (mem2 == number):
        print('member2:', "The number is", mem2)
        exit()


    if (mem3 == number):
        print('meber3:',"The number is", mem3)
        exit()
while (NotGoal == 1):

    goal_reached()

    create_child_plus_fitness()

    goal_reached()
