from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 구하는 것:
        # grid에서 1로 이루어진 섬의 둘레 길이 구하기

        row = len(grid)
        col = len(grid[0])

        perimeter = 0

        for i in range(row):
            for j in range(col):

                # 현재 칸이 땅이면
                if grid[i][j] == 1:
                    # 땅 한 칸의 기본 둘레는 4
                    perimeter += 4

                    # 위쪽에 땅이 붙어 있으면 둘레 2 감소
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # 왼쪽에 땅이 붙어 있으면 둘레 2 감소
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter