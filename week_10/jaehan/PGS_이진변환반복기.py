def solution(s):
    answer = []
    ## s가 1이 나올때 까지 
    ## 1. 0 제거, 2. 제거한 문자열의 길이를 2진법으로 표현한 문자열
    ## 위 과정을 반복
    
    ## 반환 변수
    zero_cnt = 0
    change_cnt = 0
    
    ## 0 제거 함수

    def remove_zero(my_string):
        
        nonlocal zero_cnt
        
        ## 제거할 0의 개수 카운트
        zero_cnt += my_string.count("0")
        
        ## 0 제거
        my_string = my_string.replace("0","")
        
        return my_string
    
    
    ## 2진법 변환
    def change(my_string):
        
        length = len(my_string)
        
        ## bin() -> 0b123 형태
        return bin(length)[2:]
            
    
    ## 1이 될떄까지 반복
    while s != "1":
        s = remove_zero(s)
        s = change(s)
        
        change_cnt += 1
        
    
    answer.append(change_cnt)
    answer.append(zero_cnt)
    
    
    return answer