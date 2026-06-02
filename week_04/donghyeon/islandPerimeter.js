/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    // bfs를 이용한 풀이
    // 전체 순회
    // 땅을 만나면 bfs를 이용하여 땅을 찾고
    // 땅이 붙어 있는 여부에 맞춰 둘레를 계산

    const rows = grid.length;
    const cols = grid[0].length;

    const dir = [[0,1], [1,0], [0,-1], [-1,0]];

    // 전체 순회
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                return bfs(i, j);
            }
        }
    }

    function bfs(row, col) {
        let num = 0;
        let queue = [[row, col]];

        // 방문한 지역 방문 처리(재방문 방지)
        grid[row][col] = -1;

        while (queue.length > 0) {
            const [r, c] = queue.shift();

            for (const [dr, dc] of dir) {
                const nr = dr + r;
                const nc = dc + c;

                // 땅이 붙어있는지 여부에 맞추어 둘레를 계산
                // 격자 밖 혹은 물이라면 1증가
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == 0) num++;
                else if (grid[nr][nc] == 1) {
                    queue.push([nr, nc]);
                    grid[nr][nc] = -1;
                }
            }
        }

        return num;
    }
};
