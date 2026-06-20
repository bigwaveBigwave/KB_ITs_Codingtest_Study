def rotate(key):
    """열쇠를 시계 방향으로 90도 회전하는 함수"""
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            new_key[c][m - 1 - r] = key[r][c]
    return new_key

def check(start_r, start_c, m, n, key, board):
    """열쇠가 자물쇠에 맞는지 확인하는 함수"""
    # 확장된 board에 열쇠를 더함
    for r in range(m):
        for c in range(m):
            board[start_r + r][start_c + c] += key[r][c]
            
    # 자물쇠 영역(가운데 n*n) 확인
    is_match = True
    for r in range(n):
        for c in range(n):
            # 모든 홈(0)이 1로 채워져야 하고, 돌기(1)끼리 겹치면 안 됨(2가 되면 안 됨)
            if board[m - 1 + r][m - 1 + c] != 1:
                is_match = False
                break
        if not is_match: break
    
    # 원상 복구 (백트래킹)
    for r in range(m):
        for c in range(m):
            board[start_r + r][start_c + c] -= key[r][c]
            
    return is_match

def solution(key, lock):
    m, n = len(key), len(lock)
    # 1. 자물쇠 확장: (n + 2m - 2) * (n + 2m - 2) 크기의 보드 생성
    board_size = n + (m - 1) * 2
    board = [[0] * board_size for _ in range(board_size)]
    
    # 확장된 보드 중앙에 자물쇠 배치
    for r in range(n):
        for c in range(n):
            board[m - 1 + r][m - 1 + c] = lock[r][c]
            
    # 2. 4방향 회전하며 검사
    current_key = key
    for _ in range(4):
        current_key = rotate(current_key)
        # 3. 열쇠를 이동시키며 확인
        for r in range(m + n - 1):
            for c in range(m + n - 1):
                if check(r, c, m, n, current_key, board):
                    return True
                    
    return False