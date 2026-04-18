## 괄호의 값

# 올바른 괄호열 = 괄호의 개폐가 올바른 위치에 존재
# 올바르지 않은 괄호열의 경우
# 1. (] : 서로 다른 괄호열로 개폐가 이루어진 경우
# 2. (()[] : 괄호열의 개폐가 성립되지 않는 경우

# 괄호열의 값
# 1. () = 2
# 2. [] = 3
# 3. ( x ) = 2 * x
# 4. [ x ] = 3 * x
# 5. xy = x + y

import sys

input = sys.stdin.readline
S = input().strip()

stack = []
## 값 저장용 temp
temp = 1
answer = 0

## 올바르지 않은 괄호열일 경우 마지막 출력과 분리하기 위한 플래그
is_valid = True

for i in range(len(S)) :
    s = S [i]
    # 열린 괄호 처리
    if s == "(":
        stack.append(s)
        temp *= 2
    elif s == "[":
        stack.append(s)
        temp *= 3
    
    
    ## S[i-1]을 확인하는 이유 :
    ## stack은 현재 닫는 괄호가 올바른 괄호열인지 검사하는 도구이다.
    ## 즉, 지금 들어온 닫는 괄호가 가장 최근의 열린 괄호와 짝이 맞는지만 판단할 수 있다.
    ##
    ## 하지만 (()) 처럼 중첩된 구조에서는 닫는 괄호가 나왔다고 해서
    ## 매번 값을 answer에 더하면 안 된다.
    ##
    ## 예를 들어 마지막 ')'는 stack[-1]이 '('이므로 유효한 괄호열인 것은 맞지만,
    ## 직전 문자가 '('가 아니라 ')'이므로 바로 '()'가 완성된 경우는 아니다.
    ## 즉, 이미 안쪽 값이 계산된 상태이므로 값을 또 더하면 중복 계산이 된다.
    ##
    ## 따라서 입력 문자열의 직전 문자 S[i-1]를 확인해서
    ## 바로 '()' 또는 '[]'가 완성된 경우에만 answer에 값을 더해야 한다.
    
    # 닫힌 괄호 처리
    elif s == ")" :
        ## stack이 비어있을 때
        if not stack:
            is_valid = False
            break
        ## stack의 top이 '('가 아닐 때
        if stack[-1] != "(":
            is_valid = False
            break
        if S[i-1] == "(" : 
            answer += temp 
        
        stack.pop() # pop 연산 수행 -> (()) 처럼 닫는 괄호가 연속적으로 나오는 경우를 만족
        temp //= 2 # pop 이후 다시 2로 나눔
    
    else:
        ## 대괄호도 동일하게 진행
        if not stack:
            is_valid = False
            break
        
        if stack[-1] != "[":
            is_valid = False
            break
        if S[i - 1] == "[":
            answer += temp
        stack.pop()
        temp //= 3
 
# 올바르지 않은 괄호열이었거나,
# 순회가 끝난 뒤에도 스택에 열린 괄호가 남아 있으면 0 출력

if (not is_valid) or stack :
    print(0)
else :
    print(answer)

        
            
    