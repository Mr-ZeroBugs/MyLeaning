list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Linear(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return print(i)
    return print("not found")
    
Linear(list, 5)
Linear(list, 12)