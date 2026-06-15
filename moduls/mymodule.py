def calculate_average(lst):
    if not isinstance(lst, (list, tuple)):
        raise TypeError("Аргумент должен быть списком или кортежем")
    
    if not lst:
        return None

    return sum(lst) / len(lst)