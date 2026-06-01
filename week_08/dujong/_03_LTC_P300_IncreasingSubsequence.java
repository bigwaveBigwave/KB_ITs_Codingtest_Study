class Solution {
    public int lengthOfLIS(int[] nums) {
        int N = nums.length;
        int maxLength = 1;

        int[] curOpt = new int[2501];
        curOpt[maxLength] = nums[0];

        for (int i = 1; i < N; i++) {
            if (curOpt[maxLength] < nums[i]) {
                curOpt[++maxLength] = nums[i];
            }
            else { // curOpt[maxLength] >= nums[i]
                // curOpt 배열에서 nums[i] 보다 작아지는 지점 찾기
                int index = 0;
                for (int j = maxLength; j >= 1; j--) {
                    if (curOpt[j] < nums[i]) {
                        index = j;
                        break;
                    }
                }
                curOpt[index + 1] = nums[i];
            }
        }

        return maxLength;
    }
}
