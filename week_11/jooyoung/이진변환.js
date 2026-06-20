function solution(s) {
    var answer = [];
    
    let ZeroCount = 0;
    let count = 0;
    
    while (s !== "1") {
        let words = s.split("");
        let num = [];
        
        // s에서 0 제거 후 num에 push
        for (let i of words) {
            if (i === "1") {
                num.push(1);
            } else {
                ZeroCount = ZeroCount + 1;
            }
        }
        
        // num의 길이를 2진법 문자열로 변환
        let c = num.length;
        s = c.toString(2);
        
        count = count + 1;
        console.log("변환 후 s : ", s);
    }
    
    answer = [count, ZeroCount];
    return answer;
}
