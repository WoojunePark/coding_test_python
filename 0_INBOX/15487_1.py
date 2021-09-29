import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

# N < 10^6 => N 한번 따라 도는 거도 간당간당함.
# i < j < k < l

# init
# A_j, A_i, A_l, A_k = A[1], A[0], A[3], A[2]
# Loss = A_j - A_i + A_l - A_k


for j in range(4, len(A)-4):
    # init : 0 1 2 3 '4'
    min_0_j = A[1]

    A[j] =




