## 구명보트
## 그리디 알고리즘

# 최대 2명만 태울 수 있음
# 40 50 40 60 이면 LIMIT가 100일 때 40, 40 두 명을 태우는 것이 손해
# 두 명의 몸무게가 최대한 limit를 만족해야함
# 정렬 후 limit값을 최대한 만족하는 합을 찾아서 제거

def solution(people, limit):
    answer = 0
    people.sort()
    
    left = 0
    right = len(people)-1

    while left <= right :
        # 가장 가벼운 + 가장 무거운이 limit 이하를 만족하는 경우
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
            
        # 같이 못 타면 가장 무거운 사람 혼자 탐
        else :
            right -= 1
            answer += 1
            
        # 위 두 경우 모두 보트를 1개씩 사용
        # answer += 1

    return answer

solution([70, 50, 80, 50, 40, 50, 60, 40],100)