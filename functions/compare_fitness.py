def compareFitness(value1, value2, margin=0.01):
    return abs(value1 - value2) <= margin * max(value1, value2)
