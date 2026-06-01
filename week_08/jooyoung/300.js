/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    const dp = new Array(nums.length).fill(1);

    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {        // i 앞에 있는 모든 숫자 확인
            if (nums[j] < nums[i]) {          // j가 i보다 작으면
                dp[i] = Math.max(dp[i], dp[j] + 1);  // dp[j] + 1 이 더 크면 갱신
            }
        }
    }

    return Math.max(...dp);  // dp 중에 가장 큰 값이 정답
};
