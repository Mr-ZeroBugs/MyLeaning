from collections import deque

#first in last out, latest add to the top, the top out
stack = [1, 2, 3, 4, 5]
stack.append(1)
print(stack)
print(stack.pop())

#first in first out, latest add to the top, the bottom out
queue = deque()
queue.append("A")   
queue.append("B")
print(queue)
print(queue.popleft())
