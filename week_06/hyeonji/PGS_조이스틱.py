def solution(name):
    answer = 0
    n = len(name)

    for c in name:
        up = ord(c) - ord('A')
        down = ord('Z') - ord(c) + 1
        answer += min(up, down)

    move = n - 1

    for i in range(n):

        # 현재 위치 다음부터 연속된 A 찾기
        idx = i + 1

        while idx < n and name[idx] == 'A':
            idx += 1

        # 오른쪽 갔다가 되돌아오기
        right_then_left = i * 2 + (n - idx)

        # 왼쪽 먼저 갔다가 오른쪽
        left_then_right = i + (n - idx) * 2

        move = min(move, right_then_left, left_then_right)

    return answer + move