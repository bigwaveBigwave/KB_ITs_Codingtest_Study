/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if (nums.length === 0) return 0;
    
    // dp 배열을 1로 초기화 (모든 원소는 그 자체로 길이 1인 부분 수열)
    const dp = new Array(nums.length).fill(1);
    let maxLength = 1;
    
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            // 이전 원소(nums[j])가 현재 원소(nums[i])보다 작으면 이어붙일 수 있음
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        // 가장 긴 길이를 갱신
        maxLength = Math.max(maxLength, dp[i]);
    }
    
    return maxLength;
};

// /**
//  * @param {number[]} nums
//  * @return {number}
//  */
// var lengthOfLIS = function(nums) {
//     if (nums.length === 0) return 0;
    
//     // LIS의 길이를 추적할 배열 (실제 LIS 원소와는 다를 수 있음)
//     const sub = [];
    
//     for (const num of nums) {
//         // sub 배열이 비어있거나, 현재 숫자가 맨 끝 숫자보다 크면 바로 추가
//         if (sub.length === 0 || sub[sub.length - 1] < num) {
//             sub.push(num);
//         } else {
//             // 현재 숫자가 더 작거나 같다면, 이진 탐색으로 들어갈 자리를 찾음
//             let left = 0;
//             let right = sub.length - 1;
            
//             while (left < right) {
//                 let mid = Math.floor((left + right) / 2);
//                 if (sub[mid] < num) {
//                     left = mid + 1;
//                 } else {
//                     right = mid;
//                 }
//             }
//             // 찾은 위치의 값을 더 작은 값(현재 num)으로 덮어씌움
//             sub[left] = num;
//         }
//     }
    
//     return sub.length;
// };
