function solution(n, computers) {
    var answer = 0;

    let visit = Array(n).fill(false);

    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            answer++;
            dfs(i);
        }
    }

    function dfs(index) {
        visit[index] = true;

        let computer = computers[index];

        for (let i = 0; i < computer.length; i++) {
            if (!visit[i] && computer[i] === 1) dfs(i);
        }
    }

    return answer;
}
