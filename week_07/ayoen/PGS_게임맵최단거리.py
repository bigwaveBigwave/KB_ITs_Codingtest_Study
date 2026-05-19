from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0 ,1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((0, 0 ,1))

    while q:
        x ,y, dist = q.popleft()

        # 도착점에 도착하면 최단거리 반환
        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < n and 0<=ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    q.append((nx, ny, dist+1))

    return -1