def solution(name):
    # preprocessing
    cnt_min_click_per_alp = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, cnt_total_clicks = 0, 0

    while True:
        # main
        cnt_total_clicks += cnt_min_click_per_alp[idx]  # add to cnt_total_clicks
        cnt_min_click_per_alp[idx] = 0  # zero out

        # terminal condition
        if sum(cnt_min_click_per_alp) == 0:
            break

        # next : GREEDY = partial solution
        left, right = 1, 1  #

        while cnt_min_click_per_alp[idx - left] == 0:
            left += 1
        while cnt_min_click_per_alp[idx + right] == 0:
            right += 1

        if left < right:
            cnt_total_clicks += left
            idx -= left
        else:
            cnt_total_clicks += right
            idx += right

    return cnt_total_clicks


txt = "JEROEN"

ret_num = solution(txt)
print(ret_num)
