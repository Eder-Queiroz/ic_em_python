def calculateSameClassConflicts(individual):
    sorted_individual = sorted(individual, key=lambda x: (x["day"], x["schedule"]))

    schedule_conflicts = 0
    i = 0

    while i < len(sorted_individual) - 1:
        if (
            sorted_individual[i]["class"]["id"] == sorted_individual[i + 1]["class"]["id"]
            and sorted_individual[i]["day"] == sorted_individual[i + 1]["day"]
            and sorted_individual[i]["schedule"] == sorted_individual[i + 1]["schedule"]
        ):
            schedule_conflicts += 1
            i += 1
        else:
            i += 1

    return schedule_conflicts