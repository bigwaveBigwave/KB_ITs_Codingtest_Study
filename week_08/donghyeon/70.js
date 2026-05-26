/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // 계단이 1개나 2개일 때는 n을 그대로 반환
    if (n <= 2) return n;
    
    let prev1 = 1; // n-2 번째 계단에 도달하는 방법의 수
    let prev2 = 2; // n-1 번째 계단에 도달하는 방법의 수
    
    // 3번째 계단부터 n번째 계단까지 반복하여 계산
    for (let i = 3; i <= n; i++) {
        let current = prev1 + prev2; // 현재 계단에 도달하는 방법의 수
        
        // 다음 계산을 위해 값들을 한 칸씩 앞으로 당겨줌
        prev1 = prev2;
        prev2 = current;
    }
    
    return prev2; // 최종적으로 n번째 계단에 도달하는 방법의 수가 저장
};
