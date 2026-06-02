## 섬 연결하기
## 그리디 알고리즘

# 가장 적은 비용의 다리부터 선택하되 사이클이 생기지 않게 연결

def solution(n, costs):
    # 비용 기준 정렬
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x]) # 경로 압축
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost
            
    return total_cost