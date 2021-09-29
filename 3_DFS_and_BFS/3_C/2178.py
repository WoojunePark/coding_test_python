# 찾기 -> ~FS -> 'N*M = 10000' -> BFS


import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maze = []
for y_next in range(0, N):
    maze.append(list(input().rstrip()))

dx = [1, -1, 0, 0]  # E W N S
dy = [0, 0, -1, 1]

queue = [[0, 0]]
maze[0][0] = 1

while queue:
    x_cur, y_cur = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        x_next = x_cur + dx[i]
        y_next = y_cur + dy[i]
        if 0 <= x_next < N and 0 <= y_next < M and maze[x_next][y_next] == "1":
            queue.append([x_next, y_next])
            maze[x_next][y_next] = maze[x_cur][y_cur] + 1

print(maze[N - 1][M - 1])
