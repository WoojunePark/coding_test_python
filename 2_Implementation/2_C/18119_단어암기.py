import sys


input = sys.stdin.readline


N, M = map(int, input().split())

# conditions: bit weights
vowels = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'

bit_weights = dict()
for i in range(len(cons)):
    bit_weights[cons[i]] = i


# preprocessing
words = []

for i in range(N):
    # input word
    temp = set()
    for c in input().strip():
        temp.add(c)

    # input word -> bits
    num = 0
    for c in temp:
        if c in vowels:
            continue
        else:
            num += 1 << bit_weights.get(c)

    words.append(num)


# func
current_bits = (1 << 21) - 1  # all 21-bits to 1

for i in range(M):
    o, x = input().split()

    # do
    if o == '1':
        current_bits -= 1 << bit_weights.get(x)
    else:
        current_bits += 1 << bit_weights.get(x)

    # count
    cnt = 0
    for word in words:
        if current_bits & word == word:
            cnt += 1

    # print
    print(cnt)
