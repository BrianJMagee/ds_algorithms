def binary_search(collection, target):
    low_bound = 0
    high_bound = len(collection) - 1

    while low_bound <= high_bound:
        middle = low_bound + (high_bound - low_bound) // 2
        middle_value = collection[middle]

        if target < middle_value:
            high_bound = middle - 1
        elif target > middle_value:
            low_bound = middle + 1
        else:
            return middle
    return -1
