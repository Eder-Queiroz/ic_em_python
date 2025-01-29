from functions.calculate_double_lessons import calculateDoubleLessons
from functions.calculate_same_class_conflicts import calculateSameClassConflicts
from functions.calculate_schedule_conflicts import calculateScheduleConflicts
from data.config import DOUBLE_LESSON_WEIGHT, SCHEDULES_CONFLICTS_WEIGHT, FITNESS_INITIAL_VALUE, SAME_CLASS_CONFLICTS_WEIGHT



def combinedFitness(individual):
    fitness = FITNESS_INITIAL_VALUE

    double_lessons_fitness = calculateDoubleLessons(individual) * DOUBLE_LESSON_WEIGHT
    schedule_conflicts_fitness = calculateScheduleConflicts(individual) * SCHEDULES_CONFLICTS_WEIGHT
    same_class_conflicts_fitness = calculateSameClassConflicts(individual) * SAME_CLASS_CONFLICTS_WEIGHT

    fitness += double_lessons_fitness - schedule_conflicts_fitness - same_class_conflicts_fitness

    return (fitness,)
