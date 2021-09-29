def solution(n, times):
    # think.
    # n = 10^9
    # time_takes = 10^9
    # len(eMp) = 10^5 : bingo!

    # dict? may have duplicates...
    # queue?

    # init
    N = n
    M = len(times)
    clock = 0
    few_moments = 0
    processing_table = []

    # pre
    for m in range(M):
        processing_table.append(times[m])
        # main에서는 M+1 부터 시작
        N -= 1

    people_left = N

    # main
    while True:
        print(processing_table)
        print("clock", clock)
        print("people_left", people_left)

        # 다른 자리 기다리기 vs. 지금 빈 자리 줄 서기
        # 다른 자리 :

        # case 1 : 빈자리 있음
        try:
            empty_slot = processing_table.index(0)
            processing_table[empty_slot] = times[empty_slot]

            few_moments = min(processing_table)
            for i, p in enumerate(processing_table):
                processing_table[i] -= few_moments  # no zero
            people_left -= 1

        # case 2 : 빈자리 없음
        except:
            few_moments = min(processing_table)
            for i, p in enumerate(processing_table):
                processing_table[i] -= few_moments  # no zero

        # terminal
        if people_left == 0:
            return clock

        # next
        # people_left -= 1
        clock += few_moments


sol = solution(6, [7, 10])
print("ans", sol)
