def solution(num, k):
    # [구조화 1: 스택을 이용한 그리디 탐색]
    # 숫자를 하나씩 쌓으면서 앞자리에 더 큰 숫자가 있으면 제거함
    stack = []

    for digit in num:
        # 아직 제거할 횟수(k)가 남았고, 스택에 숫자가 있으며,
        # 스택의 마지막 숫자가 현재 숫자보다 크면 제거함 (작은 숫자를 앞으로 보냄)
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # [구조화 2: 남은 제거 횟수 처리]
    # 전체를 순회했는데도 k가 남은 경우 (예: "1234", k=2), 뒤에서부터 남은 만큼 잘라냄
    if k > 0:
        stack = stack[:-k]

    # [구조화 3: 문자열 조립 및 앞자리 0 제거]
    # 리스트를 문자열로 합친 후, 좌측의 불필요한 '0'을 제거함
    # 빈 문자열이 될 경우 "0"을 반환함
    result = "".join(stack).lstrip('0')

    return result if result else "0"