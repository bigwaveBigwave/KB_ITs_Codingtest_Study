class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();

        int minMove = len - 1;

        for (int i = 0; i < len; i++) {
            char ch = name.charAt(i);

            answer += Math.min(ch - 'A', 'Z' - ch + 1);

            int next = i + 1;
            while (next < len && name.charAt(next) == 'A') {
                next++;
            }

            minMove = Math.min(minMove, i * 2 + len - next);

            minMove = Math.min(minMove, (len - next) * 2 + i);
        }

        return answer + minMove;
    }
}