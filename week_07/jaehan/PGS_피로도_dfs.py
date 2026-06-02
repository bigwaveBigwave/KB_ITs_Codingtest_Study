## 피로도
## 완전 탐색

## DFS
def solution(k, dungeons):
    answer = -1
    ## 최대한 많은 던전 탐색
    ## 탐색하면서 반복문동안 answer 최댓값 갱신
    
    visited = [False] * len(dungeons)
    max_count = [0]
    
    def dfs(curr,count):
        ## 매 탐색마다 현재까지 방문한 던전 수의 최댓값 갱신
        if count > max_count[0]:
            max_count[0] = count
        
        for i in range(len(dungeons)):
            if not visited[i] and curr >= dungeons[i][0]:
                visited[i] = True
                dfs(curr - dungeons[i][1],count+1)
                ## 백트래킹
                visited[i] = False
        
    
    dfs(k,0)
                
    return max_count[0]