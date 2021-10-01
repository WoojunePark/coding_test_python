import sys


input = sys.stdin.readline


# conditions
n, m = map(int, input().split())

up_list = []
for j in map(int, input().split()):  # 10 ** 5
    up_list.append(j)

down_list = []
for ii in range(1, n):
    up_list.pop()

    down_list[up_list[ii]] = ii

print(down_list)
print(up_list)

# func
for j in range(m):  # 10 ** 5
    i, w = map(int, input().split())

