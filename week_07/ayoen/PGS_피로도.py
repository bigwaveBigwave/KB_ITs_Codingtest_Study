def solution(k, dungeons):
    # 구하는 것:
    # 던전 순서를 잘 정했을 때 탐험할 수 있는 최대 던전 수

    answer = 0
    visited = [False] * len(dungeons)

    # energy: 현재 남은 피로도
    # count: 지금까지 탐험한 던전 수
    def dfs(energy, count):
        nonlocal answer

        # 1. 현재까지 탐험한 던전 수로 정답 갱신
        answer = max(answer, count)

        # 2. 아직 안 간 던전 중 갈 수 있는 던전을 찾는다
        for i in range(len(dungeons)):
            need, cost = dungeons[i]

            # 3. 방문하지 않았고, 현재 피로도가 최소 필요 피로도 이상이면 갈 수 있다
            if not visited[i] and energy >= need:
                visited[i] = True

                # 4. 해당 던전을 탐험하고 피로도를 소모한 상태로 다음 탐색
                dfs(energy - cost, count + 1)

                # 5. 다른 순서도 시도해야 하므로 방문 기록을 되돌린다
                visited[i] = False

    dfs(k, 0)

    return answer