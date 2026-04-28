def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    n = len(score)
    for i in range(m-1, n, m):
        answer += (score[i] * m)
    return answer