def solution(order):
    answer = 0
    stack = []  # 보조 컨테이너 벨트 (스택)
    n = len(order)

    # 1번 상자부터 n번 상자까지 순서대로 기존 컨테이너 벨트에서 나옴
    for current_box in range(1, n + 1):
        # 1. 일단 현재 상자를 보조 벨트(스택)에 넣기
        stack.append(current_box)

        # 2. 보조 벨트의 맨 위 상자가 현재 실어야 하는 상자(order[answer])와 일치하는지 확인
        # 일치한다면 일치하지 않을 때까지 계속 꺼내서 트럭에 싣기
        while stack and stack[-1] == order[answer]:
            stack.pop()  # 보조 벨트에서 상자를 꺼내고
            answer += 1  # 트럭에 실은 상자 개수 증가

    return answer