# trace back from final result

# input
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# pre
data.sort()
data_val_1st = data[n-1]
data_val_2nd = data[n-2]

cnt_1st = m // (k + 1) * k + m % (k + 1)  # k 'largest num' + 1 '2nd largest num' = (k + 1)

# init
result = 0

# main
result += cnt_1st * data_val_1st
result += (m - cnt_1st) * data_val_2nd

# post

# output
print(result)
