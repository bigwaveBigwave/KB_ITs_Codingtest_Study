## 체스판 다시 칠하기

## 색을 칠하는 경우
## 1. 맨 왼쪽 위 칸이 흰색
## 2. 맨 왼쪽 위 칸이 검정색

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

## 최솟값 갱신을 위한 값 8x8배열이므로 64번을 넘길 수 없음
min_value = 65

board = []
for _ in range(N):
    board.append(input().strip())

## 8 X 8 자르기 cut (8x8) 배열이 생성될 때마다 점검하기 위해서 반복문 내에서 최솟값 갱신
for i in range(N - 7):
    for j in range(M - 7):
        cut = [row[j:j+8] for row in board[i:i+8]]

        ## count : 칠해야 하는 횟수 세기
        count_w = 0  ## W 시작으로 만들 때 칠해야 하는 횟수
        count_b = 0  ## B 시작으로 만들 때 칠해야 하는 횟수

        ## 시작값과 k+p가 짝수인 [k][p]의 값은 같아야 함
        ## 시작값과 k+p가 홀수인 [k][p]의 값은 달라야 함
        for k in range(8):
            for p in range(8):
   
                ## 시작칸과 같은 색이어야 함
                if (k + p) % 2 == 0:
                    ## W 시작일 때
                    if cut[k][p] != "W":
                        count_w += 1
                    ## B 시작일 때
                    if cut[k][p] != "B":
                        count_b += 1
                ## 시작칸과 다른 색이어야함
                else:
                    ## W 시작일 때
                    if cut[k][p] != "B":
                        count_w += 1
                    ## B 시작일 때
                    if cut[k][p] != "W":
                        count_b += 1

        min_count = min(count_b, count_w)
        min_value = min(min_count, min_value)

print(min_value)
        
