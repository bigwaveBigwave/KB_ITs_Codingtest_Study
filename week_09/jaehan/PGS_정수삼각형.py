def solution(triangle):
    answer = -1
    
    ## dp[i][j] => i = len(triangle), j = len(triangle[i])
    ## i,j 위치에서 누적합 
    ## triange[i][j] 에서 [i][j]가 갈 수 있는 값은 [i+1][j], [i+1][j+1]
    ## 매번 최댓값을 갱신하면 마지막이 가장 큰 값임을 보장할 수 없음
    
    ## len(triangle) (트리 끝 레벨) 까지 누적합 저장 후 최댓값 비교최댓값 비교
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 왼쪽 값은 위층 맨 왼쪽 값
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            
            # 맨 오른쪽 값은 위층 맨 오른쪽 값
            elif j == len(triangle[i]) - 1 :
                triangle[i][j] += triangle[i-1][j-1]
            
            # 가운데 칸들은 왼쪽 대각 위랑 오른쪽 대각 위 합의 최댓값
            else :
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    ## triangle 마지막 레벨에서 가장 큰값 리턴
    answer = max(triangle[-1])
    
    return answer