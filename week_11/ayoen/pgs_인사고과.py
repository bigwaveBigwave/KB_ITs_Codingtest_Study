def solution(scores):
    # 완호의 점수를 따로 저장.
    wanho_attitude, wanho_peer = scores[0]
    wanho_sum = wanho_attitude + wanho_peer

    # 1순위: 근무태도 내림차순, 2순위: 동료평가 오름차순 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))

    max_peer_score = 0
    rank = 1  # 완호의 등수는 1등부터 시작해서 자기보다 높은 사람 수만큼 밀려남

    for attitude, peer in scores:
        # 내 앞의 누군가보다 동료 평가 점수가 낮다면 (근무 태도는 정렬 특성상 이미 낮거나 같음)
        if peer < max_peer_score:
            # 그런데 그 탈락자가 완호라면, 완호는 인센티브를 받지 못하므로 즉시 -1 리턴
            if attitude == wanho_attitude and peer == wanho_peer:
                return -1
            # 탈락자는 석차 계산에서 제외하므로 그냥 넘어감
            continue

        # 탈락자가 아니라면 동료 평가 최댓값을 갱신
        max_peer_score = max(max_peer_score, peer)

        # 인센티브 대상자 중에서 완호보다 총점이 높은 사람이 있다면 완호의 석차를 뒤로 밀어냄
        if attitude + peer > wanho_sum:
            rank += 1

    return rank