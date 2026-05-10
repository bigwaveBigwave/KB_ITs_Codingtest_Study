## 주유소
## 그리디 알고리즘

# 출력 : 원형으로 배치된 주유소를 한 바퀴 돌 수 있는 인덱스 값 반환

# 풀이
# gas[i] : i번째 인덱스(주유소)에서 채울 수 있는 기름양
# cost[i] : i번째 인덱스(주유소)까지 가는 데 소요되는 기름양
# 연료 탱크는 무제한
# [1,2,3,4,5] [3,4,5,1,2]
# 4 - 1 + 5 - 2 + 1 - 3 + 2 - 4 + 3 - 5 = 0
# gas[3] - cost[3] + gas[4] - cost[4] + gas[0] - cost[0] + gas[1] - cost[1] + gas[2] - cost[2]
# 1. gas의 합 - cost합이 0이상을 만족 못하는 경우 -1 리턴
# 2. 시작 인덱스 : gas[i] - cost[i] >= 0 만족
# 3. 각 인덱스에서 시작해서 원형으로 연산 
# 3번 과정 중에  양수를 만족하지 못하는 경우인 2번 기준을 만족하지 못하면 -1 리턴
# 반례 : 인덱스 4 -> 인덱스 0 -> 인덱스 1 : 3 -2 -2 = -1


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        my_sum = []
        my_idx = []
        
        ## 1번 기준 만족 -> 1번 기준이 만족된 이후부터는 항상 답이 있음을 보장할 수 있음
        if sum(gas) - sum(cost) >= 0:
            for i, (g, c) in enumerate(zip(gas, cost)): ## gas안에 같은 값이 들어갈 수 있으므로 enumerate 사용
                ## gas-cost 값을 모은 배열
                my_sum.append(g-c)
                ## 1번을 만족하면서 2번 기준 만족할 인덱스
                if g-c >= 0:
                        my_idx.append(i)
                    
        else :
            return -1
        
        
        for idx in my_idx:
            current_sum = 0
            ## 인덱스에 맞게 배열 슬라이싱 (해당 인덱스부터의 합을 순서대로(원형) 보기 위함)
            my_sum_compare = my_sum[idx:] + my_sum[:idx]
            
            is_possible = True
            for c in my_sum_compare:
                current_sum += c
                if current_sum < 0:
                    is_possible = False
                    break ## 더 이상 연산을 수행할 필요가 없으므로 다음 idx로 넘어감 
            
            if is_possible:
                return idx
            
        
    
sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))