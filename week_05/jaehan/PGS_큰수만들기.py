## 큰 수 만들기
## 그리디 알고리즘

# 정렬 불가
# 만들 수 있는 가장 큰 수
# 1. len(number)-k의 자리수를 만족
# 2. 1번을 만족하면서 첫번째 자리수가 가장 큰 수
# 2-1. number의 앞에서부터 k이하만큼 제거
# 3. 큰 수를 만족할 때까지 뒷자리까지 반복

def solution(number, k):
    
    stack = []
    
    for num in number:
        # 이전 숫자가 지금 숫자보다 작으면
        # 이전 숫자를 제거
        while stack and k > 0 and stack[-1] < num :
            stack.pop()
            k -= 1
        
        stack.append(num)
        
    # 아직 제거할 숫자가 존재할 경우 뒤에서 제거
    if k > 0 :
        stack = stack[:-k]
    

    return ''.join(stack)