# 코딩테스트 연습 > 스택/큐 > 주식가격 (stack 사용)

def solution(prices):
    # pre / init
    ans = [0] * len(prices)
    stack = []

    # main
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            # stack에 값이 있고
            # 이번 p 값이 stack의 top 값보다 작으면
            j = stack.pop()  # 그 값을 pop해서 j라고 하고
            ans[j] = i - j
            # 
        stack.append(i)
        # stack:
        # [] -> [0] -> [1] -> [2] -> [3]

    # post: 남아있는 값들 pop
    while stack:
        j = stack.pop()
        ans[j] = len(prices) - 1 - j

    return ans


prices = [1, 2, 3, 2, 3]
ret = solution(prices)
print(ret)
