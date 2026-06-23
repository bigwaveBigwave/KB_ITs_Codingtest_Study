from collections import deque


def solution(maps):
    answer = []

    max_x = len(maps)
    max_y = len(maps[0])

    # 큐는 함수 시작할 때 미리 만들어두거나, 섬을 찾았을 때 새로 만들어도 됩니다.
    # 여기서는 섬을 찾았을 때 새로 만드는 방식으로 가거나 이름을 queue로 통일합니다.
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0 for _ in range(max_y)] for _ in range(max_x)]

    for i in range(max_x):  # 💡 range 추가
        for j in range(max_y):  # 💡 range 추가
            if maps[i][j] != 'X' and visit[i][j] == 0:
                queue = deque()  # 💡 변수명 queue로 통일
                queue.append((i, j))
                visit[i][j] = 1
                total = int(maps[i][j])

                while queue:  # 💡 변수명 통일
                    x, y = queue.popleft()
                    for h in range(4):  # 💡 rnage -> range 오타 수정
                        nx = dx[h] + x
                        ny = dy[h] + y

                        if 0 <= nx < max_x and 0 <= ny < max_y:
                            # 💡 visit[nx][ny] == 0 으로 수정 (미방문 점검)
                            if visit[nx][ny] == 0 and maps[nx][ny] != 'X':
                                queue.append((nx, ny))
                                visit[nx][ny] = 1
                                total += int(maps[nx][ny])

                # 💡 while문이 완전히 끝난 후(섬 하나 탐색 완료) append 하도록 들여쓰기 수정
                answer.append(total)

    if not answer:
        return [-1]

    return sorted(answer)