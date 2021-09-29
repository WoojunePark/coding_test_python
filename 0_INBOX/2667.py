import sys

input = sys.stdin.readline

N = int(input().rstrip())

apart = []
for n in range(N):
    apart.append(list(input().split()))

dx = [1, -1, 0, 0]  # E W N S
dy = [0, 0, 1, -1]


queue = apart[[]]

while queue:
    x_cur, y_cur = queue[0][0], queue[0][1]
    del queue[0]




