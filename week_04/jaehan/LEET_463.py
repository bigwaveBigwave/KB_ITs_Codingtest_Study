## Island Perimeter - 섬 둘레

# 방문한 노드의 상하좌우에 땅이 있으면 둘레 x 상, 하, 좌, 우의 노드들이 땅인지의 여부에 따라 둘레는 4,3,2,1,0 의 값을 가짐

class Solution(object):
    def islandPerimeter(self, grid):
        n, m = len(grid), len(grid[0])
        result = 0 ## 둘레 값

        ## 왼쪽 위부터 오른쪽 아래로 내려가면서 진행하므로 아래, 오른쪽인 경우에서만 연산 수행
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 :
                    result += 4
                    
                    # 아래쪽에 땅이 있으면 맞닿은 변 2개 제거 (중복)
                    if i + 1 < n and grid[i+1][j] == 1:
                        result -= 2
                        
                    # 오른쪽에 땅이 있으면 맞닿은 변 2개 제거 (중복)
                    if j + 1 < m and grid[i][j+1] == 1:
                        result -= 2

        return result
        