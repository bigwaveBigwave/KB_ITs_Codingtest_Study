## AC

# R = 배열 요소 뒤집기 함수
# D = 첫 번째 수 버리기 ( 빈 배열에 사용 시 에러 출력 )

## 배열 입력 변환을 위한 라이브러리 모듈 import
import ast
## 덱 import
from collections import deque

S = int(input())

for s in range(S):

    ## 반복 종료 후 입력값, reverse 상태 초기화
    func = ''
    length = 0
    reverse = False
    is_error = False

    ## 입력
    func = input()
    length = int(input())
    case = deque(ast.literal_eval(input()))

    ## 출력
    for f in func:
        if f == "R":
            reverse = not reverse
        elif f == "D":
            ## 빈 배열 검증
            if not case:
                print("error")
                is_error = not is_error
                break
            ## R로 인해 역방향 연산 시 첫번째 요소 제거를 위해 덱에서 마지막 요소 제거
            if reverse:
                case.pop()
            ## R로 인해 정방향 연산 시 첫번째 요소 제거를 위해 덱에서 첫 번째 요소 제거
            else : 
                case.popleft()

    if is_error:
        continue
    else:
        if reverse :
            ## 출력 형식 맞추기
            case.reverse()
            print('[' + ",".join(map(str,case)) +']')
        else :
            print('[' + ",".join(map(str,case)) +']')

