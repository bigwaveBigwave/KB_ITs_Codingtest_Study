def solution(order):
    answer = 0

    ## 보조 컨테이너 벨트 : 번호 내림차순대로 뺄 수 있음 LIFO -> 스택
    
    box = 1
    scon = []
    
    ## for문을 돌면서 box값 증가 -> 메인 벨트의 번호를 for문이 돌때마다 체크함 (box)
    for seq in order:
        
        ## seq가 나올 때까지 박스 번호 증가시켜가면서 스택에 넣기
        while box <= seq:
            scon.append(box)
            box += 1
            
        ## 보조 컨테이너 벨트에서 맨 위 상자가 seq가 같으면 answer += 1
        if seq == scon[-1]:
            scon.pop()
            answer += 1
        
        else :
            ## 원하는 상자가 아닌데 더 이상 메인 벨트에서도 꺼낼 수 없다면
            break
                
    return answer