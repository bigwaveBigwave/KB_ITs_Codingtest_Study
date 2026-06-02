def solution(people, limit):
    # 1. 몸무게를 오름차순으로 정렬
    people.sort()

    # 2. 양 끝을 가리키는 포인터 설정
    light = 0  # 가장 가벼운 사람의 인덱스
    heavy = len(people) - 1  # 가장 무거운 사람의 인덱스

    boats = 0

    # 두 포인터가 만날 때까지 반복
    while light <= heavy:
        # 3. 가장 무거운 사람과 가벼운 사람을 같이 태울 수 있는지 확인
        if people[light] + people[heavy] <= limit:
            # 같이 탈 수 있다면 가벼운 사람 인덱스도 다음으로 이동
            light += 1

        # 4. 무거운 사람은 무조건 보트에 탑승 (혼자 타거나, 가벼운 사람과 타거나)
        heavy -= 1
        # 보트 한 대 사용 완료
        boats += 1

    return boats


# 입출력 예시 실행
print(solution([70, 50, 80, 50], 100))  # 결과: 3
print(solution([70, 80, 50], 100))  # 결과: 3