## M -> M-1 -> ... -> 1 로 돌기
# M case : 전부 다 잡기
# if L =< 2 * (max_x - min_x) + 2 * (max_y - min_y):
#     fish = M
# else:
#    M-1 case
# M-1 case :
# ///////////////
# ===> 개별 case 확인이 너무 어려움

## 1 -> 2 -> ... -> m -> ... -> M 으로 돌기
# [하나의 물고기 단위]로, 그 물고기를 포함하는 사각형들 내에서, 그 물고기를 포함한 잡은 물고기 최대값 찾기 : def get_net()
# [사각형 단위]로 안에 있는 물고기 확인하기 : def count()
# 입력 물고기가 입력 사각형 안에 있는지 확인하기 : def check()

import sys

input = sys.stdin.readline


def check(m_i_x, m_i_y, n_x_min, n_y_min, n_x_max, n_y_max):
    return n_x_min <= m_i_x <= n_x_max and n_y_min <= m_i_y <= n_y_max


def count(n_x_min, n_y_min, n_x_max, n_y_max, M_list):
    result = 0

    for m_i in M_list:
        result += check(m_i[0], m_i[1], n_x_min, n_y_min, n_x_max, n_y_max)

    return result


def get_net(m_i, L, prev_max_value, M_list):
    m_i_x, m_i_y = m_i[0], m_i[1]
    L_half = L//2   # L//2 = a + b
    max_value = prev_max_value

    for l in range(1, L_half):
        a, b = l, L_half - l
        for x in range(m_i_x - a, m_i_x + 1):  # 물고기가 사각형의 오른쪽 모서리부터 왼쪽 모서리까지
            for y in range(m_i_y - b, m_i_y + 1):
                max_value = max(max_value, count(x, y, x + a, y + b, M_list))

    return max_value


N, L, M = map(int, input().split())

M_list = []
for i in range(M):
    m_i_x, m_i_y = map(int, input().split())
    M_list.append([m_i_x, m_i_y])

prev_result = 0
result = 0
for m_i in M_list:
    result = get_net(m_i, L, prev_result, M_list)
    prev_result = result

print(result)

