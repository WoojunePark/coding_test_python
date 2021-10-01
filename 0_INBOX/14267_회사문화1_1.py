import sys


input = sys.stdin.readline


def dfs(v):
    for u in down_list[v]:
        cost[u] += cost[v]
        dfs(u)


# cond
n, m = map(int, input().split())

# input
down_list = [[] for _ in range(n + 1)]
i = 1
for up in map(int, input().split()):
    if i != 1:
        down_list[up].append(i)
    i += 1

cost = [0] * (n + 1)
for j in range(m, 0, -1):
    a, b = map(int, input().split())
    cost[a] += b

print(down_list)
print(cost)

# func
dfs(1)

# post
ans = ""
for k in range(1, n + 1):
    ans += str(cost[k]) + " "
print(ans)
