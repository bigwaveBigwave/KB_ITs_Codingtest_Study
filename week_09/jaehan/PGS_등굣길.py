def solution(m, n, puddles):
    answer = 0
    
    big = 1000000007
    
    ## dp[i][j] = (i,j)까지 도달하는 최단 경로의 수
    ## (1,1)부터 시작
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    ## puddle 리스트 set으로 변환 cuz, 탐색 속도
    puddle_set = {(x,y) for x, y in puddles}
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            ## 시작 스킵
            if i == 1 and j == 1:
                continue
                
            # 웅덩이인 경우 0으로 경로 수 설정
            if (j, i) in puddle_set:
                dp[i][j] = 0
                
            else:
                ## 오른쪽, 아래쪽 이동만 되므로 현재 위치에서 위쪽과 왼쪽에서 오는 경우를 고려
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % big
    
    
    return dp[n][m]