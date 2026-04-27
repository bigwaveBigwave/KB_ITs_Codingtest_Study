/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    // 전체 순회 하면서 1찾기
    // 찾으면 bfs 시작

    let answer = 0;
    let n = grid.length;
    let m = grid[0].length;

    // 섬은 상하좌우로 연결되므로 4방향 필요
    let dir = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] === "1") {
                // 새로운 섬 발견
                answer++;
                
                // BFS 시작: 발견한 '1'을 '0'으로 바꿔서 방문 처리 (중복 방지)
                grid[i][j] = "0"; 
                let queue = [[i, j]];

                while (queue.length > 0) {
                    let [currX, currY] = queue.shift();

                    for (let [dx, dy] of dir) {
                        let nextX = currX + dx;
                        let nextY = currY + dy;

                        // 격자 범위 내에 있고, 해당 위치가 육지('1')인 경우
                        if (nextX >= 0 && nextX < n && nextY >= 0 && nextY < m && grid[nextX][nextY] === "1") {
                            // 큐에 넣기 전에 미리 '0'으로 바꿔야 중복 방문 방지
                            grid[nextX][nextY] = "0";
                            queue.push([nextX, nextY]);
                        }
                    }
                }
            }
        }
    }

    return answer;
};
