import random
from timeit  import default_timer as timer

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else :
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

list = random.sample(range(0,10000), 10000)
start = timer()
result = quicksort(list)
end = timer()
print(end-start, "sec")

"""
1k : 0.0011441589995229151 sec
10k : 0.012125331999413902 

time : O(n log n)
space : O(log n)
"""

