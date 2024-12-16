from pprint import pprint


def calculateDoubleLessons(individual):
    sorted_individual = sorted(individual, key=lambda x: (x["day"], x["schedule"]))

    double_lessons_count = 0
    i = 0

    while i < len(sorted_individual) - 1:
        if (
            sorted_individual[i]["id"] == sorted_individual[i + 1]["id"]
            and sorted_individual[i]["day"] == sorted_individual[i + 1]["day"]
            and (
                sorted_individual[i]["schedule"] + 1
                == sorted_individual[i + 1]["schedule"]
                or sorted_individual[i]["schedule"] != 5
            )
        ):
            double_lessons_count += 1
            i += 2
        else:
            i += 1

    # return double_lessons_count * 4
    return double_lessons_count
