# BF > 2309번 : 일곱 난쟁이

import sys

input = sys.stdin.readline

# pre
heights = [int(input()) for _ in range(9)]  # 1 int per line
total_sum = sum(heights)
flag_found = False

# struct = BF: 9C2 = 36

# main
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if total_sum - 100 == heights[i] + heights[j]:
            h_i = heights[i]
            h_j = heights[j]  # 이렇게 안 받아 놓으면 인덱스 밀림
            heights.remove(h_i)
            heights.remove(h_j)
            flag_found = True
            break

    if flag_found:
        break

# post
heights.sort()
for h in heights:
    print(h)


20
7
23
19
10
15
25
8
13

# >>
# 7
# 8
# 10
# 13
# 19
# 20
# 23