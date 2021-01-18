import sys

i = 0
n = int(sys.stdin.readline().rstrip())

while i < n:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if i == 0:
        list = [[a, b]]
    else:
        list.append([a, b])
    i += 1

t = 0
j = 0
current_cost = 0

current_cost_list = sorted(list, key=lambda cost: cost[0], reverse=True)
print(current_cost_list)

while j < n:
    current_cost += current_cost_list[j][0]*t + current_cost_list[j][1]
    t += current_cost
    j += 1

print(current_cost)

