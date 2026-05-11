import java.util.Arrays;

class Leet_455 {
    public int findContentChildren(int[] g, int[] s) {
        int answer = 0;

        Arrays.sort(g);
        Arrays.sort(s);

        int n = g.length;
        int m = s.length;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++) {
                if(s[j] >= g[i]){
                    answer++;
                    s[j]=-1;//이미 준 쿠키는 -1로 만들어 다음 아이가 못가지게 함
                    break;
                }
            }
        }
        return answer;
    }
}