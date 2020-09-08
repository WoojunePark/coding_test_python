# input
n = int(input())

# pre

# init
cnt = 0

# main + input
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

# post

# output
print(cnt)

# INPUT:
# 3

# OUTPUT:
# 11475
