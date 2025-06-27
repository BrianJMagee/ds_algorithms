from linear_search import linear_search
from binary_search import binary_search


numbers = [1,2,3,4,5,6,7,8,9,10]
target = int(input("Please input a search target: "))

#index = linear_search(numbers, target)
index = binary_search(numbers, target)


if index == -1: print("Result was not found")
else: print(f"The result was found at index: {index}")