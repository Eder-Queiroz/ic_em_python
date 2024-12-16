from data.days import DAYS
from data.schedules import SCHEDULES
import random

def customMutate(individual, indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i]['schedule'] = random.randint(0, len(SCHEDULES) - 1)
        if random.random() < indpb:
            individual[i]['day'] = random.randint(0, len(DAYS) - 1)
    return individual