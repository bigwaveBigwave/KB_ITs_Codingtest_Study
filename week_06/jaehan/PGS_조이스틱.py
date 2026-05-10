## 조이스틱
## 그리디 알고리즘

# A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
 
# 풀이
# 1. 각 자리에서 A->? A->Z->? 의 값을 구해서 합산
# 2. 자리(커서) 이동 횟수 합산
# 3. Z에서 바꿀 때는 A에서 Z로 바꾸는 것이므로 값에 1을 더함 ex) Z-N+1
# Z C A A B A E

def solution(name):
    # 1번 기준. 알파벳 변경 횟수 계산 (상하)
    change_count = 0
    for char in name:
        change_count += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 2번 기준. 커서 이동 횟수 계산 (좌우)
    move = len(name) - 1 # 일단 오른쪽으로만 쭉 가는 경우로 초기화
    
    for i in range(len(name)):
        # 현재 위치 다음에 연속된 'A'가 어디까지 있는지 확인
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
            
        # [기존 move, i만큼 갔다가 되돌아가기, 뒤로 먼저 갔다가 오기] 중 최솟값 갱신
        move = min(move, i + i + len(name) - next_i, (len(name) - next_i) * 2 + i)
    
    # print(change_count + move)
        
    return change_count + move
    


solution("JEROEN")