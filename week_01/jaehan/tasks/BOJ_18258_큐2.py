## 큐 2

# queue 구현 - FIFO

# push X : 정수 X를 큐에 삽입
# pop : 큐의 가장 앞에 요소를 제거 후 출력, 빈 큐일 경우 -1 출력
# size : 큐에 들어있는 정수의 개수 출력
# empty : 큐가 비어있으면 1, 아니면 0을 출력
# front : 큐의 가장 앞에 있는 정수를 출력. 빈 큐일 경우 -1 출력
# back : 큐의 가장 뒤에 있는 정수 출력. 빈 큐일 경우 -1 출력

# 출력 명령어 한 줄당 하나씩 출력

from collections import deque
import sys

## 시간초과 방지를 위한 빠른 입력으로 변환
input = sys.stdin.readline

N = int(input())

my_queue = deque()

## 시간초과 방지를 위한 출력 변수
result = []

for n in range(N):
    command = input().split()
    if command[0] == "push" :
        my_queue.append(command[1])
    elif command[0] == "pop":
        if not my_queue:
            result.append(-1)
        else :
            result.append(my_queue[0])
            my_queue.popleft()
    elif command[0] == "size":
        result.append(len(my_queue))
    elif command[0] == "empty":
        if not my_queue:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "front":
        if not my_queue:
            result.append(-1)
        else:
            result.append(my_queue[0])
    elif command[0] == "back":
        if not my_queue:
            result.append(-1)
        else:
            result.append(my_queue[-1])

## for문 없이 join으로 출력 1회 수행
print('\n'.join(map(str,result)))