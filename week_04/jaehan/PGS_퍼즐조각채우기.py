## 퍼즐 조각 채우기

from collections import deque

def solution(game_board, table):
    n = len(game_board)
    answer = 0

    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # --------------------------------------------------
    # 1. 좌표 정규화 함수
    # --------------------------------------------------
    # BFS로 찾은 좌표들은 실제 위치가 다를 수 있다.
    #
    # 예:
    # [(4, 5), (4, 6), (5, 5)]
    #
    # 이 모양은 아래 좌표와 같은 모양이다.
    #
    # [(0, 0), (0, 1), (1, 0)]
    #
    # 그래서 가장 작은 x, y 값을 기준으로 모두 빼서
    # 좌표를 (0, 0) 근처로 옮긴다.
    #
    # 마지막에 sort()를 하는 이유:
    # BFS 탐색 순서에 따라 좌표 순서가 달라질 수 있기 때문에
    # 비교를 위해 항상 같은 순서로 정렬한다.
    # --------------------------------------------------
    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)

        normalized = []

        for x, y in shape:
            normalized.append((x - min_x, y - min_y))

        normalized.sort()
        return normalized

    # --------------------------------------------------
    # 2. BFS로 하나의 영역을 찾는 함수
    # --------------------------------------------------
    # board에서 target_value와 같은 값으로 연결된 영역을 찾는다.
    #
    # game_board에서는 target_value = 0
    # → 빈칸 영역을 찾음
    #
    # table에서는 target_value = 1
    # → 퍼즐 조각 영역을 찾음
    #
    # 반환값:
    # 연결된 좌표들의 리스트를 정규화한 결과
    # --------------------------------------------------
    def bfs(board, start_x, start_y, visited, target_value):
        queue = deque()
        queue.append((start_x, start_y))

        visited[start_x][start_y] = True

        # 현재 하나의 영역에 포함되는 좌표들을 저장
        shape = []
        shape.append((start_x, start_y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위를 벗어나면 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                # 이미 방문한 칸이면 무시
                if visited[nx][ny]:
                    continue

                # 찾고자 하는 값이 아니면 무시
                # game_board에서는 0만 찾고,
                # table에서는 1만 찾는다.
                if board[nx][ny] != target_value:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny))
                shape.append((nx, ny))

        # 위치 차이를 제거하기 위해 정규화해서 반환
        return normalize(shape)

    # --------------------------------------------------
    # 3. board에서 특정 값으로 이루어진 모든 영역 찾기
    # --------------------------------------------------
    # game_board에서 0 영역들을 찾을 때 사용
    # table에서 1 영역들을 찾을 때 사용
    # --------------------------------------------------
    def find_shapes(board, target_value):
        visited = [[False] * n for _ in range(n)]
        shapes = []

        for i in range(n):
            for j in range(n):
                # 아직 방문하지 않았고, 찾고자 하는 값이면 BFS 시작
                if not visited[i][j] and board[i][j] == target_value:
                    shape = bfs(board, i, j, visited, target_value)
                    shapes.append(shape)

        return shapes

    # --------------------------------------------------
    # 4. 퍼즐 조각 회전 함수
    # --------------------------------------------------
    # 좌표 (x, y)를 90도 회전시키는 대표 공식:
    #
    # (x, y) -> (y, -x)
    #
    # 다만 회전 후에는 음수 좌표가 생길 수 있으므로
    # 다시 normalize()를 해서 (0,0) 기준으로 맞춘다.
    # --------------------------------------------------
    def rotate(shape):
        rotated = []

        for x, y in shape:
            rotated.append((y, -x))

        return normalize(rotated)

    # --------------------------------------------------
    # 5. game_board의 빈칸들과 table의 퍼즐 조각들을 추출
    # --------------------------------------------------
    # game_board:
    # 0 = 빈칸
    # 1 = 이미 채워진 칸
    #
    # table:
    # 1 = 퍼즐 조각
    # 0 = 빈칸
    # --------------------------------------------------
    blanks = find_shapes(game_board, 0)
    pieces = find_shapes(table, 1)

    # 퍼즐 조각은 한 번만 사용할 수 있으므로 사용 여부 저장
    used = [False] * len(pieces)

    # --------------------------------------------------
    # 6. 빈칸 하나마다 맞는 퍼즐 조각 찾기
    # --------------------------------------------------
    for blank in blanks:

        # 현재 빈칸에 맞는 조각을 찾았는지 여부
        matched = False

        for i in range(len(pieces)):

            # 이미 사용한 퍼즐 조각이면 건너뜀
            if used[i]:
                continue

            piece = pieces[i]

            # 칸 개수가 다르면 절대 맞을 수 없음
            if len(blank) != len(piece):
                continue

            # 퍼즐 조각은 회전할 수 있으므로 4번 비교
            current_piece = piece

            for _ in range(4):
                # 빈칸 모양과 퍼즐 조각 모양이 같으면 매칭 성공
                if blank == current_piece:
                    used[i] = True
                    answer += len(blank)
                    matched = True
                    break

                # 90도 회전
                current_piece = rotate(current_piece)

            # 현재 빈칸에 맞는 조각을 찾았으면
            # 다른 퍼즐 조각을 더 볼 필요가 없음
            if matched:
                break

    return answer