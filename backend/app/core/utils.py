

# Noramlizes data of array from range of 0-100
def normalize (values : list[float]):
    min_value = min(values)
    max_value = max(values)
    for i in range (len(values)):
        values[i] = (values[i] - min_value) / (max_value - min_value) * 100
    return values