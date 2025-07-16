def binary_search(collection, target):
    low_index = 0
    high_index = len(collection) - 1

    count = 0
    while low_index <= high_index:
        middle_index = low_index + (high_index - low_index) // 2
        middle_value = collection[middle_index]

        count += 1
        
        if target < middle_value: high_index = middle_index - 1
        elif target > middle_value: low_index = middle_value + 1
        else: 
            print(count)
            return middle_value
    print(count)
    return -1




numbers = [8,2,4,3,9,1,6,5,7,10]
size = len(numbers)
print(f"size: {size}")
found_at = binary_search(numbers, target=5)

if found_at == -1: print("Element not found")
else: print(f"You element was found at index: {found_at}")