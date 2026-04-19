## 주어진 문자열을 모두 사용하되 적절히 더하거나 빼서 타겟 넘버를 만족하는 경우의 수
## 더하거나 빼거나의 경우만 존재

def solution(numbers, target):
    def dfs(idx, total):
        if idx == len(numbers):
            return 1 if total == target else 0 # 타겟 넘버를 만족할 때 1 반환

        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

    return dfs(0, 0) # 처음 시작 0, 처음 합계 0

# 재귀호출
## 0,0 -> index가 0일 때 그 다음 인덱스인 1에서의 요소를 더하거나 빼는 경우
## 1,+1 / 1, -1 => index가 1일 때 그 다음 인덱스인 2에서의 요소를 더하거나 빼는 경우
## ... 완전 탐색으로 더하거나 빼는 두 경우에서 마지막 요소까지 왔을 때
## target number를 만족하면 경우의 수 하나 추가 ( 1 반환 ) or 0 반환