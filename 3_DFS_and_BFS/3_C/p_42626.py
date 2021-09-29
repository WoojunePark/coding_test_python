import heapq


def solution(scoville, K):
    # pre : sort?
    cnt_act = 0
    flag_all_zero = True
    H = []

    for s in scoville:
        flag_all_zero = flag_all_zero and s == 0
        # flag_zero num
        # T 0 = T
        # T 2 = F
        # F 0 = F
        # F 2 = F
        heapq.heappush(H, s)

    if flag_all_zero:
        return -1

    # main : zip?
    while H:
        if len(H) == 1:
            return -1
        else:
            if H[0] >= K:
                return cnt_act
            else:
                least = heapq.heappop(H)
                second = heapq.heappop(H)
                new = least + (2 * second)

                heapq.heappush(H, new)
                cnt_act += 1

    # post
    # how to detect infeasible case??
    return -1


print("fin", solution([0,0,0,0,0,0,0,0], 1))
print("fin", solution([0,0,0,0,0,0,0,1], 10))
