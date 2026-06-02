## 최장 공통 부분 수열
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
       
        m, n = len(text1), len(text2)
        
        # DP 테이블 초기화 (행: m+1, 열: n+1)
        # 빈 문자열과의 비교를 위해 크기를 1씩 더 크게 잡기
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 보텀업(Bottom-up) 방식으로 DP 테이블 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 두 문자가 같다면, 이전까지의 최장 길이에 1을 더함
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 두 문자가 다르면 기존의 최댓값을 유지
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # 두 문자열 전체를 비교했을 때의 최장 공통 부분 수열의 길이 반환
        return dp[m][n]