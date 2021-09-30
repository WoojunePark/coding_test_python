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

    # 인덱스
    # 5의 직속상관이 4
    # 4의 직속상관이 3
    # 2의 직속상관이 1
    # 인덱스+1의 직속상관이 up_list[인덱스]

    # 4의 직속부하가 5
    # 3의 직속부하가 4
    # 1의 직속부하가 2

    # up_list[ii] = ii
    # up_list[4] = 4
    # up_list[1] = 1
    # up_list[0] = 0

    # down_list[3] = up_list[ii]

    down_list[up_list[ii]] = ii

print(down_list)
print(up_list)

# func
for j in range(m):  # 10 ** 5
    i, w = map(int, input().split())

