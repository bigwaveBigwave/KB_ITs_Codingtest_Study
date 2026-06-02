package LEET;

import java.util.Arrays;

public class Leet_300 {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1); //dp배열을 1로 초기화 dp=[1,1,1,1...];
        int answer = 0;

        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                if(nums[j]<nums[i]){ //j(앞의 숫자)가 i(뒤의 숫자)보다 작으면 => 증가해야하기 때문
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            answer = Math.max(answer, dp[i]);
        }
        return answer;
    }
}
