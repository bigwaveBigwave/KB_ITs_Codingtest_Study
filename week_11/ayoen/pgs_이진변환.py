def solution(s):
    change_count = 0  # 이진 변환 횟수
    zero_count = 0  # 제거된 0의 총 개수

    # s가 "1"이 될 때까지 반복합니다.
    while s != "1":
        change_count += 1  # 변환 횟수 1 증가

        num_of_zeros = s.count('0')  # 현재 문자열에서 0의 개수 구하기
        zero_count += num_of_zeros  # 누적 제거된 0의 개수에 더하기

        # 0을 제거한 후의 길이는 결국 '1'의 개수와 같습니다.
        ones_len = s.count('1')

        # 그 길이를 다시 2진법 문자열로 변환하여 s를 갱신합니다.
        # bin(6) -> '0b110' 이므로 [2:]를 통해 '110'만 가져옵니다.
        s = bin(ones_len)[2:]

    return [change_count, zero_count]