# input
n, m = map(int, input().split())
r, c, dir = map(int, input().split())

# pre
visit = [[0] * m for _ in range(n)]

move_r = [-1, 0, 1,  0]
move_c = [ 0, 1, 0, -1]


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


# init
r_new, c_new = r, c
visit[r][c] = 1
cnt_visit = 1
cnt_turn = 0

# main + input
map_array = []
for i in range(n):
    map_array.append(list(map(int, input().split())))

while True:
    # turn
    turn_left()
    r_new = r + move_r[dir]  # why r_new += move_r[dir] doesn't works?
    c_new = c + move_c[dir]

    # turn -> pre-visit land in front => go!
    if map_array[r_new][c_new] == 0 and visit[r_new][c_new] == 0:
        visit[r_new][c_new] = 1
        r, c = r_new, c_new

        cnt_visit += 1
        cnt_turn = 0
        continue

    # turn -> post-visit land or sea in front => turn!
    else:
        cnt_turn += 1

    # nowhere to go
    if cnt_turn == 4:
        r_new = r - move_r[dir]
        c_new = c - move_c[dir]

        # nowhere to go -> land => go!
        if map_array[r_new][c_new] == 0:
            r, c = r_new, c_new

        # nowhere to go -> sea => break!!
        else:
            break

        cnt_turn = 0  # why here?

# post

# output
print(cnt_visit)

# INPUT:
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# OUTPUT :
# 3
