class Solution:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0]) # 5, 5
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(sr, sc):
            stack = [(sr, sc)]
            grid2[sr][sc] = 0   # 방문 처리
            is_sub = True

            while stack:
                r, c = stack.pop()

                # grid2의 현재 섬 칸이 grid1에서는 물이면 sub-island 아님
                if grid1[r][c] == 0:
                    is_sub = False

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                        grid2[nr][nc] = 0   # 방문 처리
                        stack.append((nr, nc))

            return is_sub

        count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1

        return count