# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            # if empty queue
            # or current job requires more days than the one in queue
            Q.append([-((p-100)//s), 1])
            # => append to Q in (days, jobs to ship) format
        else:
            Q[-1][1] += 1
            # current job requires less days than the one in queue
            # => ships together
    return [q[1] for q in Q]  # return only jobs to ship


# -((p-100)//s) vs. ((100-p)//s)
# def calc_wo(p, s):
#     return (100 - p)//s
# def calc_w(p, s):
#     return -((p - 100) // s)

# calc_w(94, 4)
# 2
# calc_wo(94, 4)
# 1

