## 계단 오르기
## 매번 1, 2만 오를 수 있음
## 순서 존재

# 하향식
class Solution(object):
    def climbStairs(self, n):
        
        stairs = {}
        def dp(n):
            if n == 1:
                 return 1
            elif n == 2:
                return 2 ## [1,1], [2] 총 두가지 3이상 부터는 재귀호출로 1, 2인 경우만 생각
            
            # [메모이제이션] 이미 계산한 계단 수는 다시 계산하지 않고 재사용
            if n not in stairs:
                # n번째 계단은 (n-1)층에서 1걸음 올랐거나, (n-2)층에서 2걸음 오른 경우의 수의 합
                stairs[n] = dp(n-1) + dp(n-2)
            
            return stairs[n]

        return dp(n)

