from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 구하는 것:
        # grid에서 상하좌우로 연결된 '1' 덩어리의 개수 구하기

        # 예외 처리
        if not grid:
            return 0

        # 1. 행, 열 크기 구하기
        m = len(grid)
        n = len(grid[0])

        # 2. 섬 개수
        answer = 0

        # 3. 상하좌우 이동 방향
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 4. BFS 함수
        def bfs(x, y):
            queue = deque()
            queue.append((x, y))

            # 시작 땅 방문 처리
            grid[x][y] = "0"

            while queue:
                cx, cy = queue.popleft()

                # 상하좌우 확인
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]

                    # 범위 안이고, 땅이면 방문 처리
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))

        # 5. 전체 grid 순회
        for i in range(m):
            for j in range(n):
                # 아직 방문하지 않은 땅을 만나면 새로운 섬
                if grid[i][j] == "1":
                    answer += 1
                    bfs(i, j)

        return answer
