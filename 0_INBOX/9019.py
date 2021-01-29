import sys

T = int(sys.stdin.readline().rstrip())

case_cnt = 0

while case_cnt < T:
    A, B = map(int, input().split())

    # do A -> B
    A_filled = str(A.zfill(4))
    a_1, a_2, a_3, a_4 = A_filled[0], A_filled[1], A_filled[2], A_filled[3]

    # cond terminal : a_1, ... == b_1, ...

    # cond L,R shuffle : a_1, ... == b_1, ... (인데 순서는 다름)
    # L 이랑 R 중에 어느게 빠를지

    # cond D : B = A * 2^N
    # (B // A) % 2 == 0

    # cond S : a_1, ... == b_1, ... && a_4 < b_4
    # if A == 0:
    #     A = 9999
    # else:
    #     A -= 1

    # cond ??? : a_1, ... == b_1, ... && a_4 > b_4


    # print DSLR

    # next case!

