def solution(name):
    # [구조화 1: 알파벳 변경 횟수 계산]
    # 각 알파벳을 'A'에서 만들 때 위로 가는 것이 빠른지, 아래로 가는 것이 빠른지 계산합니다.
    # 'N'을 기준으로 이전은 위(▲), 이후는 아래(▼)가 유리합니다.
    change_count = 0
    for char in name:
        change_count += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # [구조화 2: 커서 이동 횟수 최적화]
    # 기본 이동 횟수는 한 방향으로 끝까지 가는 경우 (길이 - 1)
    n = len(name)
    move_count = n - 1

    for i in range(n):
        # 현재 위치 i 이후에 연속되는 'A'의 끝 지점(next_i)을 찾습니다.
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # [구조화 3: 세 가지 이동 경로 중 최솟값 선택]
        # 1. 순방향으로만 이동: 기존 move_count
        # 2. 뒤로 돌아가기: 현재까지 왔다가(i) 다시 원점으로 돌아가서(i) 반대방향 'A' 이후로 가기(n - next_i)
        #    공식: i + i + (n - next_i) => 2 * i + (n - next_i)
        # 3. 처음부터 뒷부분을 먼저 처리하기: 뒤를 먼저 갔다가(n - next_i) 다시 원점(n - next_i) 후 i까지 가기
        #    공식: (n - next_i) + (n - next_i) + i => 2 * (n - next_i) + i

        move_count = min(move_count, 2 * i + (n - next_i), i + 2 * (n - next_i))

    return change_count + move_count