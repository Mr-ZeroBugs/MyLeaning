import random

#useless in practice but if you cool enough:)
def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values
list = [3, 2, 1, 4, 5, 1, 2, 3, 4, 1]
print(is_sorted(list))
print(bogo_sort(list))
