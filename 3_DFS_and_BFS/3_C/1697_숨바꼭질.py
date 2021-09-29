import sys
from collections import deque


input = sys.stdin.readline


def bfs(n, k, dist, min_x, max_x):
    # init q
    q = deque()
    q.append(n)

    while q:
        # do
        x = q.popleft()

        # term
        if x == k:
            print(dist[x])
            break

        # next
        else:
            for next_x in (x-1, x+1, 2 * x):
                if min_x <= next_x <= max_x and dist[next_x] == 0:
                    dist[next_x] = dist[x] + 1
                    q.append(next_x)


# conditions
min_k = 0
max_k = 10 ** 5
distant_list = [0] * (max_k + 1)

# inputs
N, K = map(int, input().split())

# func
bfs(N, K, distant_list, min_k, max_k)
