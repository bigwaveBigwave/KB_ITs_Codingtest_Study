def solution(prices):
    # [구조화 1: 변수 초기화]
    # 누적 이익을 저장할 변수
    max_profit = 0

    # [구조화 2: 배열 순회]
    # 2번째 날(인덱스 1)부터 마지막 날까지 순회하며 전날과 가격을 비교
    for i in range(1, len(prices)):

        # [구조화 3: 차익 실현 판단]
        # 오늘 가격(prices[i])이 어제 가격(prices[i-1])보다 높다면,
        # 그 차이만큼 무조건 이익에 더하기
        if prices[i] > prices[i - 1]:
            # 어제 사서 오늘 팔았을 때의 이익을 합산
            max_profit += prices[i] - prices[i - 1]

    # [구조화 4: 결과 반환]
    # 모든 상승 구간의 차익이 합산된 값을 반환
    return max_profit