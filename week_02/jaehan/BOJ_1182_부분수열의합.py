## 부분수열의 합

import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))
path = []
count = 0    
    
## 모든 부분수열 만들기
def dfs(idx):
    global count
    if idx == len(arr):
        # print(path[:])
        if path and sum(path) == S: #공집합 제외
            count += 1
        return

    # 현재 원소 선택
    path.append(arr[idx])
    dfs(idx + 1)

    # 선택 취소 후, 현재 원소 미선택
    path.pop()
    dfs(idx + 1)

dfs(0)

print(count)