#구하는 것 : 연결된 컴퓨터 그룹 개수 구하기
# 구조화
# 1. 각 컴퓨터의 방문 여부를 저장할 visited 배열 생성
# 2. 모든 컴퓨터를 하나씩 확인
# 3. 방문하지 않은 컴퓨터 발견 시
#   - BFS 시작
#   - 연결된 모든 컴퓨터 방문 처리
#   - 그룹 개수 + 1
# 4. 모든 탐색이 끝나면 그룹 개수 출력


from collections import deque

def solution(n, computers):
    visited = [False] * n
    count = 0


    def bfs(start):
        q = deque([start])
        visited[start] = True

        while q:
            cur = q.popleft()

            for next in range(n):
                #연결 돼 있고 ,방문 안했으면
                if computers[cur][next] == 1 and not visited[next]:
                    visited[next] = True
                    q.append(next)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1

    return count