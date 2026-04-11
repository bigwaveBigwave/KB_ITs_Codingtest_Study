## 회전하는 큐

# 연산 1. 첫 번째 원소 뽑기
# 연산 2. 왼쪽으로 한 칸 이동 -> 가장 첫 번째 요소는 가장 마지막으로 이동
# 연산 3. 오른쪽으로 한 칸 이동 -> 가장 마지막 요소는 가장 첫 번재로 이동

# 주어진 순서대로 각 위치의 원소를 찾아야함
# 연산 2, 연산 3의 최소 수행 횟수 출력

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

## 인덱스
indexes = list(map(int ,input().split()))

dq = deque()

for i in range(1,N+1):
    dq.append(i)

count = 0

for target in indexes:
    ## target 위치 찾기
    index = dq.index(target)
    ## 왼쪽, 오른쪽 회전 수 체크
    left = index
    right = len(dq) - index
    ## 회전 수가 적은 방향으로 회전
    ## left = right인 경우 left로 회전 (right도 무관)
    if left <= right :
        for _ in range(left):
            count += 1
            dq.rotate(-1)
        dq.popleft()
        
    else :
        for _ in range(right):
            count += 1
            dq.rotate(1)
        dq.popleft()
        
print(count)
            
            
            
            
        
            
                
        
    

