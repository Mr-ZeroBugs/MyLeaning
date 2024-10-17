import random
from timeit import default_timer as timer

def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

list = random.sample(range(0, 10000), 10000)
start = timer()
result = selection_sort(list)
end = timer()
print(end-start, 'sec')

"""
0.02042063299995789 sec, 1k
2.2900794170000154 sec, 10k

time : O(n^2)
space : O(n)
"""
