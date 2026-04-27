function solution(rectangle, characterX, characterY, itemX, itemY) {
    var answer = 0;
    // 모든 좌표 2배 스케일 업 (0~100 범위)
    const scale = 2;
    const MAX = 101; // 50 * 2 + 1
    let map = Array.from({ length: MAX }, () => Array(MAX).fill(0));
    
    
    // 1. 경로 탐색 -> bfs 사용
    // 2. 어떻게 외곽선을 찾을건지
    // 다음으로 이동할 점의 좌표가 사각형들의 내부에 있는지 확인
    // 매번 하면 비효율이니까 matrix를 처음에
    
    // 2. 맵 그리기 (테두리는 1, 내부는 -1)
    rectangle.forEach(([x1, y1, x2, y2]) => {
        x1 *= scale; y1 *= scale; x2 *= scale; y2 *= scale;
        
        for (let i = x1; i <= x2; i++) {
            for (let j = y1; j <= y2; j++) {
                if (i > x1 && i < x2 && j > y1 && j < y2) {
                    map[i][j] = -1; // 내부는 -1로 채움
                } else if (map[i][j] !== -1) {
                    map[i][j] = 1; // 테두리는 1로 표시 (이미 내부인 곳은 건드리지 않음)
                }
            }
        }
    });
    
    // 그냥 무지성 bfs
    // 시작점 -> 종료지점 되면(종료)
    
    let dir = [[0,1],[1,0],[0,-1],[-1,0]];
    
    let queue = [[characterX * scale, characterY * scale, 0]];
    let visited = Array.from({ length: MAX }, () => Array(MAX).fill(false));
    visited[characterX * scale][characterY * scale] = true;
    
    while (queue.length > 0) {
        let [curX, curY, dist] = queue.shift();

        // 목표 지점 도달 시 리턴 (2배 했으므로 다시 2로 나눔)
        if (curX === itemX * scale && curY === itemY * scale) {
            return dist / 2;
        }

        for (let [dx, dy] of dir) {
            let nextX = curX + dx;
            let nextY = curY + dy;

            // 맵 범위 내에 있고, 테두리(1)이며, 방문하지 않은 곳
            if (nextX >= 0 && nextX < MAX && nextY >= 0 && nextY < MAX) {
                if (map[nextX][nextY] === 1 && !visited[nextX][nextY]) {
                    visited[nextX][nextY] = true;
                    queue.push([nextX, nextY, dist + 1]);
                }
            }
        }
    }
    
    return answer;
}
