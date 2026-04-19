## 연결된 컴퓨터가 있으면 1로 표현

def solution(n, computers):
    visited = [False] * n ## 각 컴퓨터를 방문했는지 체크
    answer = 0

    def dfs(x):
        visited[x] = True

        # 현재 컴퓨터 x와 인접한 컴퓨터들을 전부 방문 처리함
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)

    ## 방문하지 않은 컴퓨터를 만나면 dfs 처리하고 answer += 1
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer