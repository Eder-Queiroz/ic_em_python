
def calculatePopulationSize(lessons):
    size = 0
    for lesson in lessons:
        size += lesson['quantity']
    return size