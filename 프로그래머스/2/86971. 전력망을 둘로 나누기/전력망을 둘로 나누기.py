def solution(n, wires):
    adj = [[] for _ in range(n + 1)]
    for s, e in wires:
        adj[s].append(e)
        adj[e].append(s)
    
    subtree_size = [0] * (n + 1)
    diffs = []

    # 2. DFS를 통해 각 노드를 루트로 하는 서브트리 크기 계산
    def get_subtree_size(curr, prev):
        size = 1  # 자기 자신 포함
        for neighbor in adj[curr]:
            if neighbor != prev:  # 부모 노드로 되돌아가지 않음
                size += get_subtree_size(neighbor, curr)
        
        subtree_size[curr] = size
        
        # 3. 루트(1번)가 아닌 경우, 부모와 연결된 간선을 끊었을 때의 차이 계산
        if curr != 1:
            diffs.append(abs(size - (n - size)))
            
        return size

    # 1번 노드를 루트로 시작
    get_subtree_size(1, -1)
    
    return min(diffs)