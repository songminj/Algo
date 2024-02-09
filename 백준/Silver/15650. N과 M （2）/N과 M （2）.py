def dfs(result, i):
    # 조합의 길이가 M이 되면 결과에 추가
    if len(result) == M:
        print(*result)
        return

    # 가능한 모든 선택지에 대해 탐색
    for w in range(i, N + 1):
        # 이미 선택한 수는 건너뜀
        if w in result:
            continue
        # 현재 수를 선택하고 다음 위치로 이동
        dfs(result + [w], w+1)


# 입력 받기
N, M = map(int, input().split())

# DFS로 순열 구하기
dfs([], 1)
