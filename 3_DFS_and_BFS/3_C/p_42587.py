# 코딩테스트 연습 > 스택/큐 > 프린터

from collections import deque


def solution(priorities, location):
    # pre
    # index 와 priorities 합쳐서 enumerate
    Q = [(i, p) for i, p in enumerate(priorities)]
    ans = 0

    # main
    while True:
        cur = Q.pop(0)

        # next
        if any(cur[1] < q[1] for q in Q):
            Q.append(cur)
        else:
            ans += 1

            # terminal condition
            if cur[0] == location:
                return ans
