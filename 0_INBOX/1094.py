import sys
import heapq

X = int(sys.stdin.readline().rstrip())

Sticks = [64]

# S = 1 * 2 ** 6
# X = x_6 * 2 ** 6 + x_5 * 2 ** 5  + ... + x_0 * 2 ** 0

if sum(Sticks) > X:
    shortest = heapq.nsmallest(1, range(len(Sticks)), key=Sticks.__getitem__)

    New_sticks = Sticks
    New_sticks[shortest[0]] = New_sticks[shortest[0]] // 2

    if sum(New_sticks) >= X:
        Sticks = New_sticks
    else:
        New_sticks.append(New_sticks[shortest[0]] // 2)
        Sticks = New_sticks





