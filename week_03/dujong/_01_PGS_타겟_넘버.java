class Solution {
    static int[] numbersArr;
    static int answer;
    static int targetNum;
    
    public int solution(int[] numbers, int target) {
        // 완전탐색으로 풀 수 있는가? -> 2^20 = 대략 100만 (가능)
        // 모든 숫자를 사용해야 함 -> 종료 조건을 길이로
        
        answer = 0;
        targetNum = target;
        numbersArr = numbers;
        
        dfs(0, 0);

        return answer;
    }
    
    public static void dfs(int node, int curSum) {
        if (node == numbersArr.length) {
            if (curSum == targetNum) answer++;
            return;
        }
        dfs(node + 1, curSum - numbersArr[node]);
        dfs(node + 1, curSum + numbersArr[node]);
    }
}
