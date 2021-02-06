# STACK : FILO
#  ______________
# |
#  --------------
stack = []

stack.append(5)  # at back
stack.append(2)
stack.append(3)
stack.append(7)
# 5, 2, 3, 7

stack.pop()  # at back
# 5, 2, 3

stack.append(1)
stack.append(4)
# 5, 2, 3, 1, 4

stack.pop()
# 5, 2, 3, 1

print(stack)  # print from 'front' element
# "5, 2, 3, 1"

print(stack[::-1])  # print from 'back' element
# "1, 3, 2, 5"


# QUEUE : FIFO
#  ______________
#
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
