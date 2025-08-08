def calc_time(diff: int, level: int, time_prev: int, time_cur:int):
    if diff <= level:
        return time_cur
    else: 
        return (diff - level) * (time_cur + time_prev) + time_cur

def solution(diffs, times, limit):
    n = len(diffs)
    l, r = 1, 100001
    level = 100001
    while l <= r: 
        mid = (l + r) //2 
        total_time = 0
        for i in range(n): 
            time_prev = times[i-1] if i != 0 else 0
            total_time += calc_time(diffs[i], mid, time_prev, times[i])
        if total_time <= limit:
            level = min(mid, level)
            r = mid - 1
        else: 
            l = mid + 1
    return level