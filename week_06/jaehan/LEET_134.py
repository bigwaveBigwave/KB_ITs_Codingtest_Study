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
        
        ## 1번 기준 만족 -> 1번 기준이 만족된 이후부터는 항상 답이 있음을 보장할 수 있음
        if sum(gas) - sum(cost) >= 0:
            for g, c in zip(gas, cost):
                    my_sum.append(g-c)
                    
        else :
            return -1
        
        ## my_sum = [-2,-2,-2,3,3], [3,-2,-2,3,-2]
            
        ## 2, 3번 기준 만족 - my_sum의 합은 이미 위의 조건으로 인해 항상 0보다 크거나 같음을 만족함
        current_sum = 0
        start_index = 0
        
        # 3번 기준 : 순서대로 연산
        for idx in range(len(my_sum)):
            current_sum += my_sum[idx]
            ## 2번 기준 : 연산 값이 음수가 되는 순간 다음 인덱스로 넘김 
            ## (원형(순서)구조 -> 음수를 만족하는 인덱스부터 이전의 모든 인덱스들은 시작 인덱스를 만족할 수 없음
            ## 즉, 음수가 나온 이후 시점부터 더 이상 합이 음수가 나오지 않는 인덱스가 답을 만족하게됨
            ## cuz, my_sum은 이미 합이 0이상임을 보장한다는 전제 조건이 있기 때문에 배열 내에 음수가 되는 순간이 존재하고 그 순간 이후에 음수가 나오지 않는다면 그 시점부터는 시계방향 순환이 가능하다는게 입증됨
            if current_sum < 0:
                start_index = idx + 1
                current_sum = 0
        
        return start_index
    
sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))