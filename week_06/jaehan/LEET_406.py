## 높이에 따른 대기열 재구성
## 그리디 알고리즘

# 배열 내 0번 인덱스 값 : 그 사람의 키
# 배열 내 1번 인덱스 값 : 앞에 존재하는 키가 크거나 같은 사람의 수
# 출력 : 1번 인덱스 값을 모두 만족하는 배열로 재구성하여 출력
# 정렬 : 키 기준 내림차순 
# -> 1번 인덱스 값은 키가 크거나 같은 사람의 수이므로 작은 인원이 앞에 들어와도 무관
# -> 키가 작은 사람은 무조건 본인보다 키가 크거나 같은 사람만이 앞에 오게됨

class Solution(object):
    def reconstructQueue(self, people):
        
        answer = list()
        
        ## 정렬 -> 키 기준 내림차순 + 1번째 인덱스 기준 오름차순
        people.sort(key=lambda x: (-x[0], x[1]))
        
        ## 인덱스 값 = 내 위치 (키가 큰 인원은 인원은 본인보다 작은 인원이 앞에 올 수 있음)
        for p in people:
            answer.insert(p[1],p)

        return answer



# 클래스의 인스턴스
sol = Solution()

# 인스턴스를 통해 메서드를 호출
sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])