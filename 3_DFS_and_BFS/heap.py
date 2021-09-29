# https://www.daleseo.com/python-heapq/
# why?
# 최대값, 최소값을 빠르게 찾기 O(logN)

# how?
#

import heapq

# min_heap
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

# pop from heap
print(heapq.heappop(heap))
print(heap)
print(heapq.heappop(heap))
print(heap)

# read from heap
print(heap[0])

# turn a list into a heap
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

# max_heap
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heapq.heappop(heap)[1])  # index 1


# e.g. kth_smallest/kth_largest
def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap)
    return kth_min


def kth_largeest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    kth_max = None
    for _ in range(k):
        kth_max = heapq.heappop(heap)[1]
    return kth_max


print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
print(kth_largeest([4, 1, 7, 3, 8, 5], 3))


# e.g. heap sort
def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums


print(heap_sort([4, 1, 7, 3, 8, 5]))
