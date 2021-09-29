import sys
from collections import deque

queue = deque([])

for _ in range(int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().strip()

    if cmd[1] == 'u':
        queue.append(cmd[5:])
    elif cmd[1] == 'o':
        if queue:
            print(queue.popleft())
            continue
        print(-1)
    elif cmd[0] == 's':
        print(len(queue))
    elif cmd[0] == 'e':
        if queue:
            print(0)
            continue
        print(1)
    elif cmd[0] == 'f':
        if queue:
            print(queue[0])
            continue
        print(-1)
    elif cmd[0] == 'b':
        if queue:
            print(queue[-1])
            continue
        print(-1)
