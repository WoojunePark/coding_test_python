# input
n, k = map(int, input().split())

# pre

# init
cnt = 0

# main + input
while n != 1:
    leftover = n % k

    if leftover == 0:
        n /= k
        cnt += 1
    else:
        n -= leftover
        cnt += leftover

# post

# output
print(cnt)
