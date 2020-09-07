# input
n, m = map(int, input().split())

# pre

# init
result = 0

# main + input
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

# post

# output
print(result)
