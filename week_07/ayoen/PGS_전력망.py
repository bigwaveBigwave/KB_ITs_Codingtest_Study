# 구하는 것 : 두 전력망의 송전탑 개수 차이의 최솟값을 출력하기
# 구조화
# 1. 다 간선을 잘라봐서 차이의 최솟값을 갱신하기

from collections import deque


def solution(n, wires):
    answer = n

    # 1. 모든 전선을 하나씩 끊어본다
    for cut_a, cut_b in wires:

        # 2. 끊은 전선을 제외하고 그래프를 다시 만든다
        graph = [[] for _ in range(n + 1)]

        for a, b in wires:
            if a == cut_a and b == cut_b:
                continue

            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        cnt = 1

        while q:
            now = q.popleft()

            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
                    cnt += 1
        # 4. 한쪽 전력망 개수는 cnt, 다른 쪽은 n-cnt
        diff = abs(cnt - (n - cnt))

        # 5. 차이의 최솟값 갱신
        answer = min(answer, diff)

    return answer