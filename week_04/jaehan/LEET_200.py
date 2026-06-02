## Number of Islands

## DFS 활용 알고리즘
# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
# 3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트

class Solution(object):
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        result = 0

        def dfs(x, y):
            # 범위를 벗어나면 종료
            if x < 0 or x >= n or y < 0 or y >= m:
                return False

            # 현재 위치가 땅이면
            if grid[x][y] == "1":
                # 방문 처리
                grid[x][y] = "0"

                # 상, 하, 좌, 우 탐색
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

                return True

            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    result += 1

        return result
        