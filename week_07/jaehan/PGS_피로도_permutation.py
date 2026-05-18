## 피로도
## 완전 탐색

## permutation

import itertools
def solution(k, dungeons):
    
    answer = -1
    
    ## 순열 함수로 완전탐색을 위한 순서 리스트 생성
    my_list = list(itertools.permutations(dungeons,len(dungeons)))  
    #print(my_list)
    
    for ml in my_list:
        cur_k = k
        count = 0
        for req, use in ml:
            if req <= cur_k :
                cur_k -= use
                count += 1
                
        answer = max(answer,count)
    
    
    
    return answer