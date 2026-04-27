# 구하는 것 : 캐릭터의 현재 위치에서 아이템의 위치까지 가는 최단 경로를 구하기
# 구조화
# 1. 좌표를 2배 확대
#   - 테두리가 붙은 이동 경로 방지 위해
# 2. 직사각형 영역을 board에 표시
#   - 내부 : 1
#   - 테두리 : 2
# 3. 겹친 직사각형 때문에 내부가 된 테두리는 1로 덮어씀
# 4. 캐릭터 위치에서 아이템 위치까지 테두리 위에서만 bfs
# 5. 최종거리 나누기 2

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]

    # 1. 직사각형들을 board에 표시
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):

                # 현재 좌표가 직사각형의 테두리인 경우
                if x == x1 or x == x2 or y == y1 or y == y2:
                    # 이미 내부로 표시된 곳은 테두리로 바꾸면 안 됨
                    if board[x][y] != 1:
                        board[x][y] = 2
                # 현재 좌표가 직사각형의 내부인 경우
                else:
                    board[x][y] = 1

    # 2. 시작점과 도착점도 2배 확대
    startX = characterX * 2
    startY = characterY * 2
    targetX = itemX * 2
    targetY = itemY * 2

    # 3. BFS 준비
    q = deque()
    q.append((startX, startY, 0))

    visited = [[False] * 102 for _ in range(102)]
    visited[startX][startY] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 4. 테두리 위에서만 최단거리 탐색
    while q:
        x, y, dist = q.popleft()

        # 아이템 위치에 도착한 경우
        if x == targetX and y == targetY:
            return dist // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102:
                # 방문하지 않았고 테두리인 곳만 이동 가능
                if not visited[nx][ny] and board[nx][ny] == 2:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
