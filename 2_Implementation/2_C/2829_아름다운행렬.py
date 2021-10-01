import sys
import gc

input = sys.stdin.readline


# input
N = int(input())

arr = []
for row in range(N):  # 10 ** 2
    arr.append(list(map(int, input().split())))

# preprocess: <<diagonal>> prefix sum
A_diag_sum = [[0] * (N+1) for _ in range(N+1)]  # zero padding
B_diag_sum = [[0] * (N+1) for _ in range(N+1)]
for r in range(0, N):  # 10 ** 4
    for c in range(0, N):
        A_diag_sum[r][c] = A_diag_sum[r-1][c-1] + arr[r][c]
        B_diag_sum[r][c] = B_diag_sum[r-1][c+1] + arr[r][c]

del arr
gc.collect()  # 그냥 del 만 하면 메모리 반환은 안 함

# func
beauty_list = []  # 왜 그런진 모르겠지만 이 라인이 없으면 오히려 속도가 2배 느려짐
ans = -4000000
A_temp = 0
B_temp = 0
for L in range(1, N):
    for r in range(0, N-L):  # 10 ** 4
        for c in range(0, N-L):
            # 왼쪽, 위쪽에도 zero padding 을 했다면 이 부분을 날릴 수 있긴 함
            if r - 1 >= 0 and c - 1 >= 0:
                A_temp = A_diag_sum[r - 1][c - 1]
            else:
                A_temp = 0

            if r - 1 >= 0 and c + L + 1 <= N:
                B_temp = B_diag_sum[r - 1][c + L + 1]
            else:
                B_temp = 0

            beauty = A_diag_sum[r + L][c + L] - A_temp - (B_diag_sum[r + L][c] - B_temp)

            if beauty >= ans:
                ans = beauty
            else:
                continue

print(ans)
