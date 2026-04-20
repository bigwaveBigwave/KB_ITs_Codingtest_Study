# 구하는 것  : 각 숫자 앞에 + 나 -를 붙여서 타겟을 구하는 방법의 수
# 구조화
# 1. 숫자를 하나씩 보면서 두가지 선택(현재 숫자 더하기/현재 숫자 빼기)
# 2. 각 경우의 수를 끝까지 탐색 -> DFS
# 3. 끝까지 연산한 후 합이 target이면 방법의 개수 1 증가

def solution(numbers, target):

    def dfs(index, total):
        # 모든 숫자를 다 썼을 때
        if index == len(numbers):
            if total == target:
                return 1
            else:
                return 0

        # 현재 숫자를 더하는 경우
        plus = dfs(index + 1, total + numbers[index])

        # 현재 숫자를 빼는 경우
        minus = dfs(index + 1, total - numbers[index])

        # 두 경우의 수를 합침
        return plus + minus

    return dfs(0, 0)