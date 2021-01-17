# STACK : FILO
#  ______________
# |
#  --------------
stack =[]

stack.append(5)  # at back
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()  # at back

stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # print from front element
print(stack[::-1])  # print from back element


# QUEUE : FIFO
#  ______________
# |
#  --------------

from collections import deque  # w/ library

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

queue.append(1)
queue.append(4)
queue.popleft()

listed_queue = list(queue)
print(listed_queue)  # print in FI -> LI sequence

listed_reverse_queue = list(queue.reverse())
print(listed_reverse_queue)  # print in LI -> FI sequence
