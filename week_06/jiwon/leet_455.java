import java.util.*;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int cnt = 0;

        // 두 배열 오름차순으로 정렬 
        Arrays.sort(g);
        Arrays.sort(s);

        for(int i=0; i<g.length; i++) {
            for(int j=0; j<s.length; j++) {
                // 각 아이에 대해 최소 쿠키 크기보다 큰 쿠키 있는지 확인
                if(g[i] <= s[j]) {
                    cnt++;
                    s[j] = 0;
                    break;
                }
            }
        }

        return cnt;
    }
}