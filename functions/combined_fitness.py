from functions.calculate_double_lessons import calculateDoubleLessons
from functions.calculate_schedule_conflicts import calculateScheduleConflicts
from data.config import DOUBLE_LESSON_WEIGHT


def combinedFitness(individual):
    double_lessons_fitness = calculateDoubleLessons(individual) * DOUBLE_LESSON_WEIGHT
    #schedule_conflicts_fitness = calculateScheduleConflicts(individual)


    return (double_lessons_fitness ,)
