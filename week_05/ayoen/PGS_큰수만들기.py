def solution(number, k):
    # 숫자를 차례대로 담을 스택 생성
    stack = []

    for num in number:
        # 1. 스택에 값이 있고
        # 2. 아직 제거할 횟수(k)가 남아있으며
        # 3. 스택의 마지막 숫자보다 현재 숫자(num)가 더 크다면
        while stack and k > 0 and stack[-1] < num:
            # 스택 끝의 작은 숫자를 제거하고 k를 1 줄임
            stack.pop()
            k -= 1

        # 현재 숫자를 스택에 추가
        stack.append(num)

    # 만약 숫자를 다 돌았는데 k가 남아있는 경우 (예: "987", k=1)
    # 뒤에서부터 남은 k만큼 제거함
    if k > 0:
        stack = stack[:-k]

    # 리스트인 스택을 문자열로 합쳐서 반환
    return "".join(stack)


# 테스트 케이스 실행
print(solution("1924", 2))  # "94"
print(solution("1231234", 3))  # "3234"
print(solution("4177252841", 4))  # "775841"