import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
List = list(map(int, input().split()))


# i j k l
#   j   l 은 크게
# i   k   는 작게

# 현재 i j k l 을 알고 있다고 치자.
# init : 0 1 2 3

# 앗! 지금 본 수(List[n])가 여태 본 수 중에 제일 (incremental)

# cond 1 제일 크다 : List[l] < List[n]
# 후보군에 현재 l 추가
# l = n

# cond 2 : List[j] < List[n] < List[l]

# 여태 본 수 중에 가장 큰 수가 l
#   여태 본 수 중 두번째로 큰수가 j (j < l-1)
#   k : j < k < l 에서 가장 작은 수
#   i : i < j 에서 가장 작은 수

# 여태 본 수 중에 가장 큰 수가 j
#   여태 본 수 중 두번째로 큰수가 l (j < l-1)
#   k : j < k < l 에서 가장 작은 수
#   i : i < j 에서 가장 작은 수

print(List)

i, j, k, l = 0, 1, 2, 3

Largest = heapq.nlargest(N, range(len(List)), key=List.__getitem__)

if Largest[1] < Largest[0]:
    if Largest[1] < Largest[0] - 1:
        l = Largest[0]
        j = Largest[1]

    else:
        j_cnt = 0
        j_found = 0
        while j_found == 0:
            if Largest[2+j_cnt] < Largest[0]:
                l = Largest[0]
                j = Largest[2+j_cnt]
                j_found = 1
            else:
                j_cnt += 1

    a_l = List[l]
    a_j = List[j]

    I_searchspace = List[:j]
    I_search = heapq.nsmallest(n - 2, range(len(I_searchspace)), key=I_searchspace.__getitem__)
    i = I_search[0]

    K_searchspace = List[j + 1:l]
    K_search = heapq.nsmallest(n - 3, range(len(K_searchspace)), key=K_searchspace.__getitem__)

    k = K_search[0] + j + 1

    a_k = List[k]
    a_i = List[i]

    print(a_l, a_j, a_i, a_k)
    print(a_l + a_j - a_i - a_k)

else:
    # cond2
    print("PUFF")


