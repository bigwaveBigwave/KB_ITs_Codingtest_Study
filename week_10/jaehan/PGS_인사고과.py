def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    
    # 1. 정렬: 근무 태도(내림), 동료 평가(오름)
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    filtered_scores = []
    max_b = 0
    
    # 2. 인센티브 대상자 필터링 -> 같은 점수 내에서 동료 평가 점수가 낮은게 먼저 나옴
    ## 이미 근무 태도를 내림차순 정렬했으므로 뒤의 요소들은 앞의 요소보다 근무 태도 점수가
    ## 같거나 낮게됨, 즉 근무 태도가 낮은데 s[1] (동료 태도 점수) 까지 낮고 그 요소가 완호라면 -1 리턴, 만약 근무 태도가 앞 요소와 같다면 해당 요소는 무조건 s[1] 즉, 동료 태도 점수가 더 높으므로 인센티브 대상자로 선정될 수 있음.
    for s in scores:
        if s[1] < max_b:
            # 이 사원은 인센티브 탈락
            # 이 사원이 완호라면 -1 리턴
            if s == wanho:
                return -1
        else:
            # 이 사원은 인센티브 대상자
            max_b = max(max_b, s[1])
            filtered_scores.append(s)
            
    # 3. 석차 계산
    rank = 1
    for s in filtered_scores:
        if sum(s) > wanho_sum:
            rank += 1
            
    return rank