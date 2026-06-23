# 2차원 리스트 시계방향으로 90도 회전하는 함수
def rotate_90(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated


# 중앙의 자물쇠 영역이 모두 1인지 확인하는 함수
def check(new_lock, n):
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 1. 원래 자물쇠 크기의 3배인 새로운 보드 생성
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 보드의 정중앙에 원래 자물쇠 배치
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 2. 4방향 회전 탐색
    for rotation in range(4):
        key = rotate_90(key)  # 열쇠 90도 회전

        # 3. 열쇠를 대형 보드 위에서 한 칸씩 이동 (슬라이딩)
        # 열쇠가 자물쇠 영역에 조금이라도 걸치려면 0부터 n*2까지만 돌면 됩니다.
        for x in range(n * 2):
            for y in range(n * 2):

                # 4. 열쇠를 보드에 끼워 넣기 (더하기)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 5. 자물쇠가 열리는지 검사
                if check(new_lock, n):
                    return True

                # 6. 안 열리면 다음 탐색을 위해 열쇠를 다시 빼기 (원상복구)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False