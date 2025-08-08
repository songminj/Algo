def solution(info, n, m):
    t = len(info)
    answer = 121
    from functools import lru_cache

    @lru_cache(None)
    def dfs(idx : int, a : int, b : int):
        nonlocal answer
        if a >= n or b >= m:
            return
        if a >= answer:
            return
        if idx == t:
            answer = min(answer, a)
            return 
        dfs(idx+1, a + info[idx][0], b)
        dfs(idx+1, a, b+info[idx][1])
    
    dfs(0, 0, 0)
    return -1 if answer == 121 else answer
    
    