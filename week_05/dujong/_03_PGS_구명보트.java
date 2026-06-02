import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        //이중반복문: 최악의 경우 N^2 -> 25억번 연산 -> 사용 불가
        //보트 하나에 최대 2명 -> 투포인터를 활용해서 탑승하면 포인터 업데이트
        
        Arrays.sort(people);
        
        int answer = 0;
        int index1 = 0;
        int index2 = people.length - 1;
        
        while (index1 < index2) {
            if (people[index1] + people[index2] <= limit) {
                index1++;
                index2--;
            } else {
                index2--;
            }
            answer++;
        }
        
        if (index1 == index2) {
            answer++;
        }
        
        return answer;
    }
}
