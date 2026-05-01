from collections import deque

def solution(maps):
    answer = []
    r = len(maps)
    c = len(maps[0])
    visited = [[False] * c for _ in range(r)]
    mv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def bfs(x, y):
        total = 0
        queue = deque([(x, y)])
        while queue:
            curr_x, curr_y = queue.popleft()
            total += int(maps[curr_x][curr_y])
            for nx, ny in mv: 
                dx, dy = curr_x + nx, curr_y + ny
                if 0 <= dx < r and 0 <= dy < c:
                    if not visited[dx][dy] and maps[dx][dy] != 'X':
                        visited[dx][dy] = True
                        queue.append((dx, dy))
        answer.append(total)
        return 
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
    answer.sort()
    return answer if answer else [-1]