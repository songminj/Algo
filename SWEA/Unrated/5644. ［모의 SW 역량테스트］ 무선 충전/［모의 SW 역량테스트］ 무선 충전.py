
# p1, p2가 이동하면서 배터리 방문
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]


def move(t):
    global p1_now, p2_now, energy
    # 현재 위치에서 충전기 검색
    docharge1 = []
    docharge2 = []
    for i in range(1, a + 1):
        # 가능한 충전기의 번호와 power를 list에 넣어준다
        if abs(p1_now[0] - (bc[i][1] - 1)) + abs(p1_now[1] - (bc[i][0] - 1)) <= bc[i][2]:
            docharge1.append([i, bc[i][3]])
        if abs(p2_now[0] - (bc[i][1] - 1)) + abs(p2_now[1] - (bc[i][0] - 1)) <= bc[i][2]:
            docharge2.append([i, bc[i][3]])
    # 성능을 기준으로 sort
    docharge1 = sorted(docharge1, key=lambda x: (-x[1], x[0]))
    docharge2 = sorted(docharge2, key=lambda x: (-x[1], x[0]))

    # 두개가 동시에 충전 가능한경우
    if docharge1 and docharge2:
        pass
        tmp = 0
        if docharge1[0][0] == docharge2[0][0]:
            if len(docharge1) > 1 and len(docharge2) > 1:
                tmp1 = docharge1[0][1] + docharge2[1][1]
                tmp2 = docharge1[1][1] + docharge2[0][1]
                energy += max(docharge1[0][1], tmp1, tmp2)
            elif len(docharge1) > 1 and len(docharge2) == 1:
                tmp = docharge1[1][1] + docharge2[0][1]
                energy += max(docharge1[0][1], tmp)
            elif len(docharge2) > 1 and len(docharge1) == 1:
                tmp = docharge1[0][1] + docharge2[1][1]
                energy += max(docharge1[0][1], tmp)
            elif len(docharge1) == 1 and len(docharge2) == 1:
                energy += docharge1[0][1]
        else:
            energy += (docharge1[0][1] + docharge2[0][1])
    # 1번만 충전기 안에 들어왔다.
    elif docharge1 and not docharge2:
        energy += docharge1[0][1]
    # 2번만 충전기 안에 들어왔다.
    elif docharge2 and not docharge1:
        energy += docharge2[0][1]
    # print('p1', docharge1, 'p2', docharge2)
    # print('energy', energy)
    # 다음 이동 위치
    if t < m:
        p1_now[0], p1_now[1] = p1_now[0] + di[p1[t]], p1_now[1] + dj[p1[t]]
        p2_now[0], p2_now[1] = p2_now[0] + di[p2[t]], p2_now[1] + dj[p2[t]]


test_case = int(input())
for T in range(1, test_case + 1):
    # m : 이동시간, A : 배터리 개수
    m, a = map(int, input().strip().split())

    # p1, p2: 사용자 1, 2
    p1 = list(map(int, input().split()))  # (0, 0) 에서 시작
    p2 = list(map(int, input().split()))  # (9, 9) 에서 시작
    p1_now = [0, 0]
    p2_now = [9, 9]

    # 충전기 정보 [x, y, 충전거리, 충전량]
    bc = {}
    # 충전기가 그려진 지도를 만든다
    road = [[0] * 10 for _ in range(10)]
    for i in range(1, a + 1):
        bc.setdefault(i, list(map(int, input().split())))
        road[bc[i][1] - 1][bc[i][0] - 1] = i
    energy = 0
    for t in range(m + 1):
        move(t)
    print(f'#{T} {energy}')
