## 쿠키 할당
## 그리디 알고리즘

# 풀이
# 1. 쿠키는 인당 한 개씩만 할당
# 2. 한 개씩 할당이므로 쿠키의 크기와 탐욕 지수가 매칭(쿠키 크기가 탐용지수보다 크거나 같음)되는 최대 횟수를 리턴
# 3. 만족한 아이들의 최대 숫자는 쿠키 배열의 크기를 벗어날 수 없음
# 반례 : [1,2,4,5], [1,3,5] 일 때 5를 2에 할당하면 3은 1에 할당되고 1은 만족할 수 없어서 최대값을 리턴할 수 없음
# 4. 반례에 의해서 정렬된 상황일 때 쿠키는 본인보다 작거나 같은 아이 중 최댓값에 할당해야함
# 5. 즉, 정렬된 상황에서 아이는 쿠키 배열을 탐색하면서 조건을 만족하는 최솟값을 가져가야 하므로 순서대로 탐색하면서 조건을 만족하는 순간 +1

class Solution(object):
    def findContentChildren(self, g, s):
        
        answer = 0
        
        # 정렬(오름차순)
        g.sort()
        s.sort()
        
        child_idx = 0
        cookie_idx = 0
        

        while (child_idx < len(g) and cookie_idx < len(s)):
            if g[child_idx] <= s[cookie_idx]:
                answer += 1
                child_idx += 1
                
            # 쿠키 할당 여부와 상관없이 다음 쿠키로 이동
            cookie_idx += 1
            
        return answer
    
sol = Solution()
sol.findContentChildren([1,2,3],[1,2])
        