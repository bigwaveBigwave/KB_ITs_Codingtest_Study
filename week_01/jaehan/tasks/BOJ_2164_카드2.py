## 카드 2

# 제일 위의 카드를 버린 뒤 그 다음 제일 위의 카드를 스택의 가장 아래로 이동
# 마지막 남은 카드 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
my_stack = deque()
result = []

for n in range(1,N+1):
    my_stack.append(n)

while len(my_stack) > 1:
    ## 제일 위 카드 제거
    my_stack.popleft()
    ## 제거 후 제일 위 카드 아래로 이동
    temp = my_stack[0]
    my_stack.popleft()
    my_stack.append(temp)

print(''.join(map(str,my_stack)))
    
    
    