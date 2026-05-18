## 전력망을 둘로 나누기
## 완전 탐색

from collections import deque
def solution(n, wires):
    ## wires의 길이는 n-1, n은 2 이상 100이하 자연수
    ## 전력망을 두개로 나누었을 때(간선을 하나만 끊으면 만족됨) 각 전력망의 개수가 가장 비슷
    
    ## 최솟값 갱신을 위해 큰 값으로 초기화
    answer = float('inf')
    
    ## 연결 리스트 생성 -> 간선 갱신마다 사용하기 위해서 함수로 선언
    def make_graph(wires):
        graph = [[] for _ in range(n+1)]
    
        for a, b in wires:
            graph[a].append(b)
            graph[b].append(a)
        
        return graph
    
    ## bfs
    def bfs(graph,start):
        visited = [0] * (n+1)
        
        q = deque()
        q.append(start)
        visited[start] = 1
        cnt = 1 
        
        while q:
            cur_node = q.popleft()
            
            for nxt_node in graph[cur_node]:
                if visited[nxt_node] == 0:
                    visited[nxt_node] = 1
                    q.append(nxt_node)
                    cnt += 1 ## 방문하면 개수 증가
        
        return cnt
        

    
    ## 완전 탐색 -> 간선을 하나씩 끊어보기
    ## wires 배열에서 그래프를 하나씩 빼면서 bfs 수행
    ## 송전탑 개수가 나오면 2개중 다른 하나의 네트워크 개수는 n에서 해당 개수를 빼면 됨
    ## 차이가 가장 작은 값 리턴
    for i in range(len(wires)):
        wires_re = wires[:i] + wires[i+1:]
        current_graph = make_graph(wires_re)
        ## 송전탑은 간선 하나를 끊으면 무조거 두 개로 고정되며
        ## 송전탑 번호를 1로 고정해도 2개의 송전탑의 크기를 구할 수 있음
        group1_count = bfs(current_graph,1)
        group2_count = n - group1_count
        
        diff = abs(group1_count - group2_count)
        
        answer = min(answer,diff)
        
        
        # print(current_graph)
        
    
    return answer