import numpy as np

def take(array, count):
    return array[:count]

def chunks(array, size):
    if not size > 0:
        raise Exception('Size must be greater than 0')

    return [array[i:i+size] for i in range(0, len(array), size)]

def contains(array, candidate):
    for element in candidate:
        if not element in array:
            return False

    return True

def have_same_elements(a, b):
    return sorted(a) == sorted(b)

def occurrences(a_list):
    unique, counts = np.unique(np.array(a_list), return_counts=True)
    return dict(zip(unique, counts))

def available_in(stock, demand):
    stock_counts = occurrences(stock)
    demand_counts = occurrences(demand)

    for item, count in demand_counts.items():
        available_count = stock_counts[item]
        if available_count <= count:
            return False

    return True

def filter_list(a_function, a_list):
    return list(filter(a_function, a_list))
