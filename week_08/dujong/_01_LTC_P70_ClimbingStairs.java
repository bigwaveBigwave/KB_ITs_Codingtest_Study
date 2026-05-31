class Solution {
    public int climbStairs(int n) {
        // D[n] : n을 만들 수 있는 총 가짓수
        // n에 도착하려면 n-1에서 1을 더하거나 n-2에서 2를 더해야 한다
        // 따라서 D[n] = D[n-1] + D[n-2]
        // D[1] = 1, D[2] = 2, ....
        
        int[] D = new int[n+1];

        if (n == 1) {
            return n;
        }
        D[1] = 1;
        D[2] = 2;

        for (int i = 3; i <= n; i++) {
            D[i] = D[i-1] + D[i-2];
        }

        return D[n];
    }
}
