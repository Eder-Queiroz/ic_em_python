import random
from data.days import DAYS
from data.schedules import SCHEDULES

def lessonsToIndividuals(lessons):
    individual = []
    for lesson in lessons:
        for i in range(lesson['quantity']):
            schedulesIndex = random.randint(0, len(SCHEDULES) - 1)
            daysIndex = random.randint(0, len(DAYS) - 1)
            
            individual.append({
                **lesson,
                "schedule": schedulesIndex,
                "day": daysIndex,
            })
    return individual