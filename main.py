from deap import base, creator, tools, algorithms
from functions.calculate_population_size import calculatePopulationSize
from functions.lessons_to_individuals import lessonsToIndividuals
from functions.generate_schedule_and_day import generateScheduleAndDay
from functions.combined_fitness import combinedFitness
from functions.custom_mutate import customMutate
from functions.compare_fitness import compareFitness
import random
import matplotlib.pyplot as plt
from pprint import pprint as p

# Importa suas aulas de lesson.py
from data.lessons import lessons
from data.config import POPULATION_SIZE, MAX_GENERATIONS, P_CROSSOVER, P_MUTATION, TOURNAMENT_SIZE, RANDOM_SEED

random.seed(RANDOM_SEED)

toolbox = base.Toolbox()
toolbox.register("LessonsToIndividuals", lessonsToIndividuals, lessons)

initialIndividuals = toolbox.LessonsToIndividuals()

toolbox.register("GenerateScheduleAndDay", generateScheduleAndDay, initialIndividuals)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox.register(
    "individualCreator",
    tools.initRepeat,
    creator.Individual,
    toolbox.GenerateScheduleAndDay,
    len(initialIndividuals),
)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

toolbox.register("evaluate", combinedFitness)

toolbox.register("select", tools.selTournament, tournsize=TOURNAMENT_SIZE)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", customMutate, indpb=1.0 / POPULATION_SIZE)

population = toolbox.populationCreator(n=POPULATION_SIZE)

generationCounter = 0

fitnessValues = list(map(toolbox.evaluate, population))
for individual, fitnessValue in zip(population, fitnessValues):
    individual.fitness.values = fitnessValue


fitnessValues = [individual.fitness.values[0] for individual in population]

maxFitnessValues = []
meanFitnessValues = []

best_individual = tools.selBest(population, 1)[0]

# Lista para armazenar os valores do fitness máximo das últimas 10 gerações
last_10_max_fitness = []

while generationCounter < MAX_GENERATIONS:
    generationCounter = generationCounter + 1

    offspring = toolbox.select(population, len(population) - 1)
    offspring = list(map(toolbox.clone, offspring))

    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < P_CROSSOVER:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < P_MUTATION:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    freshIndividuals = [ind for ind in offspring if not ind.fitness.valid]
    freshFitnessValues = list(map(toolbox.evaluate, freshIndividuals))
    for individual, fitnessValue in zip(freshIndividuals, freshFitnessValues):
        individual.fitness.values = fitnessValue

    offspring.append(best_individual)

    population[:] = offspring

    fitnessValues = [ind.fitness.values[0] for ind in population]
    maxFitness = max(fitnessValues)
    meanFitness = sum(fitnessValues) / len(population)
    maxFitnessValues.append(maxFitness)
    meanFitnessValues.append(meanFitness)
    print(
        "- Generation {}: Max Fitness = {}, Avg Fitness = {}".format(
            generationCounter, maxFitness, meanFitness
        )
    )

    current_best_individual = tools.selBest(population, 1)[0]
    if current_best_individual.fitness.values[0] > best_individual.fitness.values[0]:
        best_individual = toolbox.clone(current_best_individual)

    # Adicionar o valor do fitness máximo atual à lista
    last_10_max_fitness.append(maxFitness)
    if len(last_10_max_fitness) > 10:
        last_10_max_fitness.pop(0)
    '''
    # Verificar se todos os valores na lista são iguais
    if len(last_10_max_fitness) == 10 and all(
        f == last_10_max_fitness[0] for f in last_10_max_fitness
    ):
        print("Fitness não mudou por 10 gerações. Interrompendo o loop.") 
        break  '''

best_index = fitnessValues.index(max(fitnessValues))
print("Best Individual = ", population[best_index])

plt.plot(maxFitnessValues, color="red")
plt.plot(meanFitnessValues, color="green")
plt.xlabel("Generation")
plt.ylabel("Max / Average Fitness")
plt.title("Max and Average Fitness over Generations")
plt.show()
