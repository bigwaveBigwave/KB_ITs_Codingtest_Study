class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= i; j++) {

                if (j == 0) {
                    // 맨 왼쪽은 바로 위에서만 내려올 수 있음
                    triangle[i][j] += triangle[i - 1][j];

                } else if (j == i) {
                    // 맨 오른쪽은 왼쪽 위에서만 내려올 수 있음
                    triangle[i][j] += triangle[i - 1][j - 1];

                } else {
                    // 가운데는 왼쪽 위 / 오른쪽 위 중 큰 값 선택
                    triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
                }
            }
        }

        int answer = 0;

        for (int num : triangle[n - 1]) {
            answer = Math.max(answer, num);
        }

        return answer;
    }
}