import random
from data.days import DAYS
from data.schedules import SCHEDULES
from pprint import pprint

current_individual = 0

def generateScheduleAndDay(individuals):
    global current_individual

    if current_individual >= len(individuals):
        current_individual = 0
        
    individual = individuals[current_individual]

    schedulesIndex = random.randint(0, len(SCHEDULES) - 1)
    daysIndex = random.randint(0, len(DAYS) - 1)
    individual['schedule'] = schedulesIndex
    individual['day'] = daysIndex

    current_individual += 1
    
    return individual