import random

#generate a population for arrangement
def generate_population(size):
    population = []
    
    for i in range(size):
        #generate the arrangement of 8 queens on the board
        arrangement = [random.randint(0, 7) for _ in range(8)]
        population.append(arrangement)
    return population

#calculate the fitness of arrangement
def fitness(arrangement):
    conflicts = 0
    
    for i in range(len(arrangement)):
        for j in range(i + 1, len(arrangement)):
            #check for conflicts between queens in the same row
            if arrangement[i] == arrangement[j]:
                conflicts += 1
            
            #check for conflicts between queens diagonally
            offset = j - i
            if arrangement[i] == arrangement[j] - offset or arrangement[i] == arrangement[j] + offset:
                conflicts += 1
    return conflicts

#select the parents for the next generation
def selection(population, num_parents):
    parents = []
    
    for i in range(num_parents):
        fitnesses = [fitness(arrangement) for arrangement in population] # Calculate the fitness of each arrangement
        index = fitnesses.index(min(fitnesses))  # Select the arrangement with the lowest fitness
        parents.append(population[index])
        population.pop(index) #remove the selected arrangement to avoid selecting it again
        
    return parents

#perform crossover between two parents
def crossover(parent1, parent2):
    midpoint    = random.randint(1, 6) #choose a random midpoint for the crossover
    child       = parent1[:midpoint] + parent2[midpoint:] #create a child with the combination of parent1 and parent2
    
    return child

#perform mutation (random changes)
def mutation(arrangement):
    #choose 2 random index to swap
    index1, index2 = random.sample(range(8), 2)
    arrangement[index1], arrangement[index2] = arrangement[index2], arrangement[index1]

#run the G.A.
def genetic_algorithm(population_size, num_parents, num_generations):
    #generate an initial population
    population = generate_population(population_size)
    
    #loop through each generation
    for generation in range(num_generations):
        parents = selection(population, num_parents) #select parents for next generation
        offspring = [] #create new offspring population
        
        #keep generating offspring until new population = old population
        while len(offspring) < population_size:
            parent1, parent2 = random.sample(parents, 2) #choose 2 from the selected parents
            child = crossover(parent1, parent2) #create a child by crossover
            
            #mutation on the child with a probability of 0.1
            if random.random() < 0.1:
                mutation(child)
            offspring.append(child) #add the child to the new population
            
        population = offspring #for te next generation
    
    #calculate the fitness of each arrangement 
    fitnesses = [fitness(arrangement) for arrangement in population]
    index = fitnesses.index(min(fitnesses))
    return population[index]

def print_solution(arrangement):
    for i in range(len(arrangement)):
        row = ["_"] * len(arrangement)
        row[arrangement[i]] = "Q"
        print(" ".join(row))

best_arrangement = genetic_algorithm(population_size=100, num_parents=10, num_generations=100)
print_solution(best_arrangement)