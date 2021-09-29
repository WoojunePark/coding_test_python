import sys
from collections import deque


input = sys.stdin.readline


def bfs(n, k, dist, cnt, min_x, max_x):
    # init
    dist[n] = 0
    cnt[n] = 1

    # init q
    q = deque()
    q.append(n)

    while q:
        # do
        x = q.popleft()

        # term
        if x == k:
            print(dist[x])
            print(cnt[x])
            break

        # next
        else:
            for next_x in (x-1, x+1, 2 * x):
                if min_x <= next_x <= max_x:
                    # first visit
                    if dist[next_x] == -1:
                        dist[next_x] = dist[x] + 1
                        cnt[next_x] = cnt[x]
                        q.append(next_x)

                    # not first visit
                    else:
                        if dist[next_x] == dist[x] + 1:
                            cnt[next_x] += cnt[x]


# conditions
min_k = 0
max_k = 10 ** 5
distant_list = [-1] * (max_k + 1)
count_list = [0] * (max_k + 1)

# inputs
N, K = map(int, input().split())

# func
bfs(N, K, distant_list, count_list, min_k, max_k)
