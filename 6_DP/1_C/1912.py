# DP > 1912번: 연속합

import sys

input = sys.stdin.readline

# pre
N = int(input().rstrip())
A = [int(x) for x in input().split()]

# struct: DP
mem = [A[0]]
ans = A[0]

# main
for i, a in enumerate(A):
    if i == 0:
        pass
    else:
        mem.append(max(mem[i - 1] + a, a))
        ans = max(ans, mem[i])

# post
print(ans)