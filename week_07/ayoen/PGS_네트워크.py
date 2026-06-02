def solution(n ,computers):
    answer = 0
    visited = [False] * n

    def dfs(com_idx):
        visited[com_idx] = True

        for connect_idx in range(n):
            if computers[com_idx][connect_idx] == 1 and not visited[connect_idx]:
                dfs(connect_idx)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                answer += 1

        return answer