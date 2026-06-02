from collections import deque

def solution(game_board, table):
    n = len(game_board)

    # 구하는 것:
    # game_board의 빈칸(0)에 table의 퍼즐 조각(1)을 회전해서 맞출 때
    # 최대로 채울 수 있는 칸 수

    # 구조화:
    # 1. game_board에서 0으로 연결된 빈칸 덩어리를 찾는다.
    # 2. table에서 1로 연결된 퍼즐 조각 덩어리를 찾는다.
    # 3. 각 덩어리 좌표를 (0, 0) 기준으로 정규화한다.
    # 4. 퍼즐 조각을 90도씩 회전하면서 빈칸 모양과 비교한다.
    # 5. 맞는 조각이 있으면 사용 처리하고 칸 수를 더한다.

    def bfs(board, target):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = True

                    shape = []

                    while q:
                        x, y = q.popleft()
                        shape.append((x, y))

                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]

                            if 0 <= nx < n and 0 <= ny < n:
                                if not visited[nx][ny] and board[nx][ny] == target:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))

                    shapes.append(normalize(shape))

        return shapes

    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)

        result = []
        for x, y in shape:
            result.append((x - min_x, y - min_y))

        return sorted(result)

    def rotate(shape):
        # (x, y)를 90도 회전하면 (y, -x)
        rotated = []

        for x, y in shape:
            rotated.append((y, -x))

        return normalize(rotated)

    blanks = bfs(game_board, 0)
    blocks = bfs(table, 1)

    used = [False] * len(blocks)
    answer = 0

    for blank in blanks:
        for i in range(len(blocks)):
            if used[i]:
                continue

            block = blocks[i]

            for _ in range(4):
                if blank == block:
                    answer += len(blank)
                    used[i] = True
                    break

                block = rotate(block)

            if used[i]:
                break

    return answer