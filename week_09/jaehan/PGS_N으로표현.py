def solution(N, number):
    answer = 0
    ## 8번까지만 가능 -> 8번 전부 사칙연산 수행해서 리턴
    
    if N == number :
        return 1
    
    ## N을 i번 썼을 때 나오는 숫자들의 집합
    dp = [set() for _ in range(9)]
    
    ## 8번 수행
    for i in range(1,9):
        ## 1. N을 i번 이어 붙인 수 (ex) 1, 11, 111 ...)
        dp[i].add(int(str(N) * i))
        
        ## 2. 이전 집합들을 조합해서 사칙연산하기
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        ## number 만족 시 횟수 리턴
        if number in dp[i]:
            return i
    
    ## for문을(8번) 다해도 안나오면 -1 리턴
    return -1