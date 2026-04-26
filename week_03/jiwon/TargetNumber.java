package week_03.jiwon;

public class TargetNumber {

    static int count = 0;    

    public int targetNumber(int[] numbers, int target) {
        count = 0;
        int num_length = numbers.length;
        
        dfs(0, numbers, 0, num_length, target);
        
        return count;
    }
    
    public static void dfs(int idx, int[] numbers, int sum, int length, int target) {
        
        // 종료 조건 : 모든 숫자 확인한 경우
        if(idx == length) {
            // 합이 target과 같은 경우 count++ 
            if(sum == target) {
                count++;
            }
            return;
        }
        
        // 1) 현재 인덱스의 값에 + 부호 적용하는 경우
        dfs(idx + 1, numbers, sum+numbers[idx], length, target);
        
        // 2) - 부호 적용하는 경우
        dfs(idx + 1, numbers, sum-numbers[idx], length, target);
    }

    public static void main(String[] args) {
        TargetNumber t = new TargetNumber();

        // 테스트 케이스 1
        int[] numbers1 = {1, 1, 1, 1, 1};
        int target1 = 3;
        System.out.println("Test Case 1: " + t.targetNumber(numbers1, target1)); // 예상 결과: 5

        // 테스트 케이스 2
        int[] numbers2 = {4, 1, 2, 1};
        int target2 = 4;
        System.out.println("Test Case 2: " + t.targetNumber(numbers2, target2)); // 예상 결과: 2
    }
}
