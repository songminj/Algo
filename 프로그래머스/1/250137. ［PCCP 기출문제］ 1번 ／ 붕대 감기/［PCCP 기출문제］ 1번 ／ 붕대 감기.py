def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    now = health
    attack_dict = {time: damage for time, damage in attacks}
    cnt = 0 

    for time in range(1, attacks[-1][0] + 1):
        if time in attack_dict:
            now -= attack_dict[time]
            if now <= 0:
                return -1
            cnt = 0
        else:
            now = min(max_health, now + x)
            cnt += 1
            if cnt == t:
                now = min(max_health, now + y)
                cnt = 0

    return now