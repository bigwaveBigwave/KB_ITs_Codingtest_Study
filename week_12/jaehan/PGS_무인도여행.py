from collections import deque
def solution(maps):
    
    answer = []
    
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    
    # print(visited)
    
    # 방향
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    ## bfs
    def bfs(start_r, start_c):
        q = deque()
        visited[start_r][start_c] = True
        cnt = int(maps[start_r][start_c])
        q.append([start_r, start_c])
        
        while q:
            cur_row, cur_col = q.popleft()
            
            for i in range(4):
                nr, nc = cur_row + dr[i], cur_col + dc[i]
                if 0 <= nr < row and 0 <= nc < col:
                    if maps[nr][nc] != "X" and not visited[nr][nc]:
                        cnt += int(maps[nr][nc])
                        visited[nr][nc] = True
                        q.append([nr, nc])
        
        # while 종료 후
        return cnt
            
        
    
    ## bfs 수행
    for r in range(row):
        for c in range(col):
            if not visited[r][c] and maps[r][c] != "X":
                answer.append(bfs(r, c))
                
    
    answer = sorted(answer)
    
    if not answer :
        return [-1]
    else : 
        return answer