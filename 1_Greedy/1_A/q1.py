# 큰 수의 법칙 - 1

# input
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# pre
data.sort()
data_val_largest = data[n-1]
data_val_2nd_largest = data[n-2]

# init
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += data_val_largest
        m -= 1
    if m == 0:
        break
    result += data_val_2nd_largest
    m -= 1

# output
print(result)


