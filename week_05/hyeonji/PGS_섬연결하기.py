def solution(n, costs):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            parent[root_b] = root_a
            return True

        return False

    costs.sort(key=lambda x: x[2])

    answer = 0

    for a, b, cost in costs:
        if union(a, b):
            answer += cost

    return answer