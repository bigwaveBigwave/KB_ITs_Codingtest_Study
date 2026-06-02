//큰수를 찾으려면 맨 앞자리가 제일 커야함

import java.util.*;
class pg_큰수만들기 {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < number.length(); i++){
            char num = number.charAt(i); // 하나씩 불러옴

            //k가 남아있고, 앞의 숫자가 존재, 앞의 숫자가 지금 보다 작으면
            while(k > 0 && sb.length() > 0 && sb.charAt(sb.length() - 1) < num){
                sb.deleteCharAt(sb.length() - 1);
                k--; //숫자를 지웠을때만 횟수를 차감하도록
            }
            sb.append(num);
        }
        if (k > 0) {
            sb.setLength(sb.length() - k); // 이미 큰 순서대로 정렬 돼있을때
            // k만큼 뒤에서 잘라냄
        }
        return sb.toString();
    }
}