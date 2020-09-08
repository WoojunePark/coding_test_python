# input
input = input()  # input = input().split()  ==> 'a', '1'
r = int(ord(input[0])) - int(ord('a')) + 1
c = int(input[1])

# pre
# moves_r = [-1,  1, -1,  1, -2, -2,  2,  2]
# moves_c = [-2, -2,  2,  2,  1, -1,  1, -1]
moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

# init
r_new, c_new = r, c
number_of_moves = 0

# main + input
for move in moves:
    r_new += move[0]
    c_new += move[1]
    if 1 <= r_new <= 8 and 1 <= c_new <= 8:
        number_of_moves += 1

# post

# output
print(number_of_moves)

# INPUT :
# a1

# OUTPUT :
# 2
