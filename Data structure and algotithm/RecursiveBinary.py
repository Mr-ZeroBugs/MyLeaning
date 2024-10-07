#functional programming, worse perfomance(in some languages like python), easier to read
#Time = O(log n)
#Space = O(log n)

import numpy as np

def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else :
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else :
            if target > list[midpoint]:
                return recursive_binary(list[midpoint+1:], target) #call itself until it found
            else :
                return recursive_binary(list[:midpoint], target)

list = np.linspace(1, 10, 10)
test = recursive_binary(list, 10)
print(test)