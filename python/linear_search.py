def linear_search(collection, target):
    for i in range(len(collection)):
        if target == collection[i]:
            return i
    else: return -1

#len() produces the size of the array, starting from 1
#but range() by default starts from 0, which makes it useful for indexing


"""✅ **len()** just tells you how many elements are in a collection.

✅ **range(n)** produces a sequence of numbers starting at 0 by default, not because of len()"""