import sys


input = sys.stdin.readline

# input
N = int(input())

arr = []
for row in range(N):  # 10 ** 2
    arr_row = list(map(int, input().split()))
    arr.append(arr_row)


# func
beauty = []

for n in range(1, N):  # 10 ** 2

    # do
    for r_start in range(N - n):  # 10 ** 2
        for c_start in range(N - n):  # 10 ** 2
            A = 0
            B = 0
            for ii in range(n+1):  # 10 ** 2
                A += arr[r_start + ii][c_start + ii]
                B += arr[r_start + ii][c_start + n - ii]
            beauty.append(A-B)


print(max(beauty))
