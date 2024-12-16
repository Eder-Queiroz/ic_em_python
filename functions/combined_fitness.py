from functions.calculate_double_lessons import calculateDoubleLessons
from functions.calculate_schedule_conflicts import calculateScheduleConflicts


def combinedFitness(individual):
    double_lessons_fitness = calculateDoubleLessons(individual)
    schedule_conflicts_fitness = calculateScheduleConflicts(individual)
    # schedule_conflicts_fitness = 0

    return (double_lessons_fitness - schedule_conflicts_fitness,)
