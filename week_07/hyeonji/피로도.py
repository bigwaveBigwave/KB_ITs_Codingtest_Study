from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for case in permutations(dungeons):
        tired = k
        count = 0
        
        for need, use in case:
            if tired >= need:
                tired -= use
                count += 1
        
        answer = max(answer, count)
    
    return answer