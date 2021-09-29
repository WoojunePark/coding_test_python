# 코딩테스트 연습 > 정렬 > H-index

def solution(citations):
    # pre
    sorted_citations = sorted(citations, reverse=True)
    N = len(citations)
    # [6, 5, 3, 1, 0]

    # main
    for h in range(sorted_citations[0], -1, -1):
        cnt_cited_more_than_h = 0
        cnt_cited_less_than_h = 0

        for i, c in enumerate(sorted_citations):
            if h <= c:
                cnt_cited_more_than_h += 1
            if h > c:
                cnt_cited_less_than_h += 1
        # terminal
        if cnt_cited_more_than_h >= h and (N - cnt_cited_more_than_h == cnt_cited_less_than_h):
            return h