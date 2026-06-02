def solution(new_id):
    #1단계 : 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    #2단계: 소문자, 숫자, -,_,.을 제외한 모든 문자를 제거
    answer = ''
    for char in new_id:
        if char.isalnum() or char in '-_.':
            answer += char
    # 3단계 : 마침표가 2번 이상 연속된 부분을 하나로 치환
    while '..' in answer:
        answer = answer.replace('..','.')

    #4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = answer.strip('.') # strip은 양 끝의 특정 문자를 제거

    #5단계 : 빈 문자열이라면 "a" 대입
    if not answer:
        answer = "a"

    #6단계 : 길이가 16자 이상이면 처음 15개만 남김
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')

        #7e단계 : 길이가 2자 이하라면 마지막 문자를 길이가 3이 될때까지 반복
        while len(answer) < 3:
            answer += answer[-1]

        return answer