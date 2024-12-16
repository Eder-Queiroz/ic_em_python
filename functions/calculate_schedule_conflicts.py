def calculateScheduleConflicts(individual):
    sorted_individual = sorted(individual, key=lambda x: (x["day"], x["schedule"]))

    schedule_conflicts = 0
    i = 0

    while i < len(sorted_individual) - 1:
        if (
            sorted_individual[i]["id"] != sorted_individual[i + 1]["id"]
            and sorted_individual[i]["day"] == sorted_individual[i + 1]["day"]
            and sorted_individual[i]["schedule"] == sorted_individual[i + 1]["schedule"]
            and sorted_individual[i]["classroom"]["id"]
            == sorted_individual[i + 1]["classroom"]["id"]
        ):
            schedule_conflicts += 1
            i += 2
        elif (
            sorted_individual[i]["id"] == sorted_individual[i + 1]["id"]
            and sorted_individual[i]["day"] == sorted_individual[i + 1]["day"]
            and sorted_individual[i]["schedule"] == sorted_individual[i + 1]["schedule"]
        ):
            schedule_conflicts += 1
            i += 2
        else:
            i += 1

    return schedule_conflicts
