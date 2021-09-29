import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_list = []

for line in range(0, N):  # 10^4
    word = list(input().rstrip())
    alp_cnt_list_temp = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

    for alp in word:  # 10^3 -> 26
        num = ord(alp) - 97
        alp_cnt_list_temp[num] += 1

    word_list.append([1, [], alp_cnt_list_temp])


cnt_words_full = 0
list_forgot = []

for q in range(0, M):  # 5x10^4
    o, _, x = list(input().rstrip())
    num = ord(x) - 97
    cnt_words_full = 0
    cnt_words_full_temp = 0

    if o == '1':  # forget
        for word in word_list:
            if word[2][num] == 1:
                word[2][num] = -1
                word[0] = 0

            # list_forgot.append([num, N - cnt_words_full])

    else:  # remember
        # for l in list_forgot:
        #     if l[0] == num:
        #         cnt = l[1]
        #
        # cnt_words_full = cnt_words_full_temp + cnt

        for word in word_list:
            if word[2][num] == -1:
                word[2][num] = 1

        for word in word_list:
            if word[2].count(-1) == 0:
                word[0] = 1
    #
    #         print(word[0])
    # print("\n")

    for word in word_list:
        if word[0] == 1:
            cnt_words_full += 1

    print(cnt_words_full)
    # cnt_words_full_temp = cnt_words_full

