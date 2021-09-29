# 코딩테스트 연습 > DFS/DFS > 타겟 넘버

from itertools import product


def solution(num, tgt):
    # pre : sort?
    cnt_target_ways = 0
    N = len(num)
    list_sorted_num = sorted(num, reverse=True)

    # main : zip?
    for p in product([-1, 1], repeat=N):
        partial_sum = 0
        for i, n in enumerate(list_sorted_num):
            partial_sum += p[i] * n

        if partial_sum == tgt:
            cnt_target_ways += 1

    return cnt_target_ways
