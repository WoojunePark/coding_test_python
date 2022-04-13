import sys
import itertools
import math

input = sys.stdin.readline


# input
n, m = map(int, input().split())
# m은 서로 다름!

if m == 0:
    sun_list = []
else:
    sun_list = list(map(int, input().split()))

# func : count possible numbers
# n = 4, m = 0
# 9 x 10 x 10 x 10

# n = 4, m = 1
# 1 x 10 x 10 x 10  +  10 x 1 x 10 x 10  +  10 x 10 x 1 x 10  +  10 x 10 x 10 x 1

# n = 4, m = 2
# 1 x 1 x 10 x 10  +  1 x 10 x 1 x 10  +  1 x 10 x 10 x 1  +  10 x 1 x 1 x 10  +  10 x 1 x 10 x 1  +  10 x 10 x 1 x 1
# nPm * (10 ** 2)

# n = 2, m = 2
# 1 x 1 + 1 x 1
# nPm * (10 ** 0)

# 2P1 * (10 ** (2-1)) = 2 * 10 - 1
# 2P2 * (10 ** (2-2)) = 2 * 1 - 0

# nPm * (10 ** (n-m)) - (n-m)
print(int(math.factorial(n) / math.factorial(n-m) * (10 ** (n-m)) - (n-m)))

# count = 0
# for c in cases:
#     if c[0] == 0:
#         continue
#     else:
#         count += 1
#
# # print : len(possible_numbers)
# print(count)
