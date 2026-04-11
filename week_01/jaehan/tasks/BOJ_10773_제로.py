## 제로

# 정수가 0일 경우 지울 수 있는 수가 존재함을 보장함
# 정수가 0일 경우 가장 최근 수 제거

K = int(input())
my_stack = []

for k in range(K):
    cost = int(input())
    
    if cost == 0:
        ## 0 이전 가장 최근 수 제거
        my_stack.pop()
    else :
        my_stack.append(cost)
        

print(sum(my_stack))