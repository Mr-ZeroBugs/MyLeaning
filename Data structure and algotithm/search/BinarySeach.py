#Time = O(log n)
#space = O(1)

import numpy as np

def binary(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return print(midpoint)
        elif target > list[midpoint]:
            first = midpoint + 1
        elif target < list[midpoint] :
            last = midpoint - 1

    return print("not found")


list = np.linspace(1, 10, 10)
binary(list, 4)
list = ['a', 'b', 'c', 'd', 'e', 'f']
binary(list, 'c')