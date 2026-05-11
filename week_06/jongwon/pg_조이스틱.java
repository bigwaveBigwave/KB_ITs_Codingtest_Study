import java.util.*;

class pg_조이스틱 {
    public int solution(String name) {
        int answer = 0;
        int n = name.length();
        int move = n - 1; //기본(끝까지 오른쪽으로 이동)

        for(int i=0; i < n; i++) {
            //상하 조작
            char target = name.charAt(i);
            answer += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);
            //좌우 조작
            int nextIndex = i + 1;
            while (nextIndex < n && name.charAt(nextIndex) == 'A') {
                nextIndex++;
            }

            move = Math.min(move, i * 2 + n - nextIndex);
            move = Math.min(move, (n - nextIndex) * 2 + i);
        }

        return answer + move;

    }
}