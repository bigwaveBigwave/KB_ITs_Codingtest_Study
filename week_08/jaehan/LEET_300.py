## 가장 긴 증가 부분 수열

from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):

        if not nums:
            return 0
            
        sub = []
        for num in nums:
            # num이 들어갈 수 있는 가장 왼쪽 위치를 이진 탐색으로 찾음
            idx = bisect_left(sub, num)
            
            # 만약 sub의 맨 뒤에 들어가야 한다면 원소 추가
            if idx == len(sub):
                sub.append(num)
            # 그렇지 않다면 해당 위치의 값을 더 작은 값(num)으로 대체
            else:
                sub[idx] = num
                
        return len(sub)