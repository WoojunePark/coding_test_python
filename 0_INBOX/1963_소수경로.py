import sys
from collections import deque


input = sys.stdin.readline


def bfs(cur, dest, moves, primes):
    # init q
    q = deque()
    q.append(cur)

    while q:
        # do
        x = q.popleft()

        # term
        if x == dest:
            print(moves[x])
            break

        # next
        else:
            digits = []
            for j in str(x):
                digits.append(j)

            possible_nums = []
            for k in range(4):
                for l in range(10):
                    digits[k] = str(l)
                    num = int(digits[0]) * 1000 + int(digits[1]) * 100 + int(digits[2]) * 10 + int(digits[3])

                    if num in primes and num != x:
                        possible_nums.append(num)

            for next_x in possible_nums:
                if moves[next_x] == 0:
                    moves[next_x] = moves[x] + 1
                    q.append(next_x)


# pre
n = 9999
isPrime = [False, False] + [True] * (n - 1)
primes = []

for i in range(1000, n + 1):
    if isPrime[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            isPrime[j] = False

# input
T = int(input())

for i in range(T):
    move_list = [0] * n

    prime_a, prime_b = map(int, input().split())

    print(prime_a, prime_b)
    # func
    bfs(prime_a, prime_b, move_list, primes)
