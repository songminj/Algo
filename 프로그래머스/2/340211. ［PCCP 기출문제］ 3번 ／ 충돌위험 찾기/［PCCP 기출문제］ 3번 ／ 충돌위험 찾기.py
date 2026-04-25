from collections import Counter

def solution(points, routes):
    # 1. 포인트 좌표 정보 정리 (1번 포인트부터 시작)
    point_dict = {i + 1: points[i] for i in range(len(points))}

    # 각 로봇의 시간대별 위치를 저장할 리스트
    # robot_paths[robot_idx] = [(r0, c0), (r1, c1), ...]
    robot_paths = []
    
    for route in routes:
        path = []
        # 첫 번째 포인트 설정
        curr_r, curr_c = point_dict[route[0]]
        path.append((curr_r, curr_c))
        
        # 다음 경유지들로 이동
        for i in range(1, len(route)):
            target_r, target_c = point_dict[route[i]]
            
            # r 좌표부터 이동 (최단 경로 & r 우선 원칙)
            while curr_r != target_r:
                if curr_r < target_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                path.append((curr_r, curr_c))
            
            # 그 다음 c 좌표 이동
            while curr_c != target_c:
                if curr_c < target_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                path.append((curr_r, curr_c))
        
        robot_paths.append(path)
    # 2. 시간대별로 충돌 체크
    answer = 0
    max_time = max(len(p) for p in robot_paths)
    
    for t in range(max_time):
        positions_at_t = []
        for path in robot_paths:
            # 해당 로봇이 t초에 아직 운행 중이라면 위치 추가
            if t < len(path):
                positions_at_t.append(path[t])
        
        # 해당 시간대에 각 좌표별 로봇 수 계산
        count = Counter(positions_at_t)
        
        # 2대 이상 있는 좌표의 개수 추출
        for pos in count:
            if count[pos] >= 2:
                answer += 1
                
    return answer