def solution(n, costs):
    # 1. 비용을 기준으로 오름차순 정렬 (Greedy approach)
    costs.sort(key=lambda x: x[2])

    # 2. 각 섬의 부모 노드를 자기 자신으로 초기화 (Union-Find 준비)
    parent = [i for i in range(n)]

    # [함수] 부모 노드를 찾는 함수 (Path Compression 적용)
    def find(parent, x):
        if parent[x] == x:
            return x
        # 재귀적으로 최상위 부모를 찾고 업데이트하여 경로 단축
        parent[x] = find(parent, parent[x])
        return parent[x]

    # [함수] 두 섬을 하나로 합치는 함수
    def union(parent, a, b):
        rootA = find(parent, a)
        rootB = find(parent, b)
        # 더 작은 번호를 가진 노드를 부모로 설정 (일관성)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB

    total_cost = 0
    bridge_count = 0

    # 3. 비용이 적은 다리부터 하나씩 확인
    for island1, island2, cost in costs:
        # 두 섬의 최상위 부모가 다르다면 (즉, 아직 연결되지 않았다면)
        if find(parent, island1) != find(parent, island2):
            union(parent, island1, island2)  # 두 섬을 연결
            total_cost += cost  # 비용 추가
            bridge_count += 1  # 연결된 다리 개수 증가

            # 모든 섬이 연결되면 (간선 수 = n-1) 종료
            if bridge_count == n - 1:
                break

    return total_cost


# 입출력 예시 실행
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # 결과: 4