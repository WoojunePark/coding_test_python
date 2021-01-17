# input
n = int(input())
# plans = map(str, input().split())
plans = input().split()

# pre
moves = ["U", "D", "L", "R"]
dc = [-1, 1,  0, 0]
dr = [ 0, 0, -1, 1]

# init
c, r = 1, 1
c_new, r_new = c, r

# main
for plan in plans:

    # calc planned move
    for move in range(len(moves)):
        if plan == moves[move]:
            c_new = c + dc[move]
            r_new = r + dr[move]

    # check condition
    if c_new < 1 or c_new > n or r_new < 1 or r_new > n:
        continue
    else:
        # follow the plan
        c, r = c_new, r_new

# post

# output
print(c, r)


# INPUT :
# 5
# R R R U D D

# OUTPUT :
# 3 4
