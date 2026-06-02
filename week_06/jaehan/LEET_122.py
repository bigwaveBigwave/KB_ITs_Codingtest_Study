## 주식 사고팔기
## 그리디 알고리즘

# 출력 : 배열 요소들을 순서대로 감가하여 최대 이익을 출력

# 풀이
# 시간 순서로 진행
# 하루에 여러번 매도/매수할 수 있으므로 그날 팔고 산 뒤에 다음 날 또 팔 수 있으므로 지금보다 비싼 경우면 무조건 팔아야함

class Solution(object):
    def maxProfit(self, prices):
        
        result = 0
        days = len(prices) 
        
        for i in range(days-1):
            if prices[i+1] - prices[i] > 0:
                result += prices[i+1] - prices[i]
        
        
        return result