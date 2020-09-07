# input
n, k = map(int, input().split())

# pre

# init
cnt = 0

# main + input
while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

# post

# output
print(cnt)
