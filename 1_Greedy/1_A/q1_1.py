# 큰 수의 법칙 -2
import time

# input
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# start_time = time.time()

# pre
data.sort()
data_val_1st = data[n-1]
data_val_2nd = data[n-2]

full_seq = data_val_1st * k + data_val_2nd

cnt_full_seq = m // (k+1)
cnt_partial_seq = m % (k+1)

# init
result = 0

# main
result += cnt_full_seq * full_seq
result += cnt_partial_seq * data_val_1st

# end_time = time.time()
# time_taken = end_time - start_time

# output
print(result)
# print(time_taken)
