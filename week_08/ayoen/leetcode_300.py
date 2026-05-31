class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # 모든 위치에서의 최소 LIS 길이는 1
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                # 앞의 원소(j)가 현재 원소(i)보다 작다면 증가 수열 가능
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 전체 dp 배열 중 가장 큰 값이 정답
        return max(dp)