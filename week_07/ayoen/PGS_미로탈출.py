from collections import deque
def solution(maps) :
    n = len(maps)
    m = len(maps[0])

    start = lever = end = None

    # S, L, E 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    def bfs(start, target):
        dx = [-1, 0 ,1, 0]
        dy = [0,1 , 0, -1]

        visited = [[False] * m for _ in range(n)]
        q = deque()

        sx, sy = start
        q.append((sx, sy, 0))
        visited[sx][sy] = True

        while q:
            x, y, time = q.popleft()

            if (x, y) == target:
                return time

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx, ny, time+1))
        return -1

    s_l = bfs(start, lever)

    if s_l == -1:
        return -1

    l_e = bfs(lever, end)

    if l_e == -1:
        return -1

    return s_l + l_e