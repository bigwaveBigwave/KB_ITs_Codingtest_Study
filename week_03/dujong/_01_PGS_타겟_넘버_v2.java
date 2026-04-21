class Solution {
    static int[] numbersArr;
    static int answer;
    static int targetNum;
    static int totalSum;

    public int solution(int[] numbers, int target) {
        targetNum = target;
        numbersArr = numbers;
        answer = 0;

        // 전체 합을 먼저 계산 (부호가 모두 +)
        totalSum = 0;
        for (int num: numbers) {
            totalSum += num;
        }

        // 전체 합이 target과 같으면 조기 return
        if (totalSum == target) {
            answer++;
            return answer;
        }
        
        // 순차적으로 배열의 숫자에 - 부호를 붙이면서 dfs로 탐색
        for (int i = 0; i < numbers.length; i++) {
            dfs(i, totalSum);
        }
        return answer;
    }

    public static void dfs(int node, int curSum) {
        int updatedSum = curSum - 2 * numbersArr[node];
        
        if (updatedSum == targetNum) {
            // 업데이트된 합이 타겟과 같으면 answer++ 후 탐색 중단
            answer++;
            return;
        } else if (updatedSum < targetNum) {
            // 업데이트된 합이 타겟보다 작아지면 탐색 중단
            return;
        } else {
            // 업데이트된 합이 타겟보다 큰 경우 이후 index부터 추가 탐색
            for (int i = node + 1; i < numbersArr.length; i++) {
                dfs(i, updatedSum);
            }
        }
    }
}
