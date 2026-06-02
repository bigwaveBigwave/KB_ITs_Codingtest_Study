def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(x):
        visited[x] = True
        
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer