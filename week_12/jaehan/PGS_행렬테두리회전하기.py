def solution(rows, columns, queries):
    answer = []
    
    ## 1. 행렬 생성
    matrix = [ [0] * columns for _ in range(rows)]
    current_value = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = current_value
            current_value += 1
            
    # print(matrix)
    
    ## 2. 쿼리 처리 (실제 인덱스 값이랑 맞추기) + 회전 로직
    my_queries = []
    for x1, y1, x2, y2 in queries:
        
        # 쿼리 값 변환
        r1, c1, r2, c2 = x1-1, y1-1, x2-1, y2-1
        
        # 회전 시작
        # 테두리 값들을 시계방향 순서대로 추출
        border = []
        # 위쪽 행
        for j in range(c1, c2): border.append(matrix[r1][j])
        # 오른쪽 열
        for i in range(r1, r2): border.append(matrix[i][c2])
        # 아래쪽 행
        for j in range(c2, c1, -1): border.append(matrix[r2][j])
        # 왼쪽 열
        for i in range(r2, r1, -1): border.append(matrix[i][c1])
        
        # 최솟값 저장
        answer.append(min(border))
        
        # 리스트 회전 (마지막 요소를 앞으로 보냄) (시계방향이므로)
        # 예: [1, 2, 3] -> [3, 1, 2]
        border = [border[-1]] + border[:-1]
        
        # 회전된 값을 다시 행렬에 채우기
        idx = 0
        for j in range(c1, c2): matrix[r1][j] = border[idx]; idx += 1
        for i in range(r1, r2): matrix[i][c2] = border[idx]; idx += 1
        for j in range(c2, c1, -1): matrix[r2][j] = border[idx]; idx += 1
        for i in range(r2, r1, -1): matrix[i][c1] = border[idx]; idx += 1
        
    return answer