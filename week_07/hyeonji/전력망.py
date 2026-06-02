from collections import deque

def solution(n, wires):
    answer = n
    
    for cut in wires:
        graph = [[] for _ in range(n + 1)]
        
        for a, b in wires:
            if [a, b] == cut or [b, a] == cut:
                continue
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        q = deque([1])
        visited[1] = True
        count = 1
        
        while q:
            cur = q.popleft()
            
            for next in graph[cur]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
                    count += 1
        
        other = n - count
        answer = min(answer, abs(count - other))
    
    return answer