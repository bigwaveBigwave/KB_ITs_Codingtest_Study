## k 숫자 제거
## 그리디 알고리즘

class Solution(object):
    def removeKdigits(self, num, k):
        
        stack = []
        
        for n in num:
            
            while stack and k > 0 and stack[-1] > n :
                stack.pop()
                k -= 1
                
                
            stack.append(n)
            
        # 아직 제거할 숫자가 존재할 경우 뒤에서 제거
        if k > 0 :
            stack = stack[:-k]
        
        # 리스트 문자열로 합치기
        # 맨 앞 "0" 제거
        # 만약 결과가 빈 문자열이면 0 리턴
        result = ''.join(stack).lstrip("0")
        result = result if result else "0"
            
        # print(result)
        return result
    
    
sol = Solution()
sol.removeKdigits("10200",1)
            
        