//arr -> table or game_board, k -> 1(블록) or 0(빈칸)
function bfs(start, arr, k) {
    let needvisit = start;
        
    let block = [];
    const dx = [0,0,1,-1];
    const dy = [1, -1, 0, 0];
        
    while (needvisit.length > 0) {
        let [cx, cy] = needvisit.shift();
        block.push([cx, cy]);
        arr[cx][cy] = k;
            
        for (let i=0; i<4; i++) {
            let nx=cx+dx[i];
            let ny=cy+dy[i];
                
            if (nx<0||nx>=arr.length||ny<0||ny>=arr.length) continue;
            else if(arr[nx][ny] === k) continue;
            else {
                needvisit.push([nx, ny]);
                arr[nx][ny] = k;
            }
        }
    }
    
    block = blockmove(block, arr.length);
        
    return block;
}

function blockmove(block, k) {
    let minx = Infinity;
    let miny = Infinity;

    for (let i = 0; i < block.length; i++) {
        if (minx > block[i][0]) minx = block[i][0];
        if (miny > block[i][1]) miny = block[i][1];
    }

    return block.map(pos => [pos[0] - minx, pos[1] - miny]);
}

function rotate(block) {
    // 1. 90도 회전 (x, y) -> (y, -x)
    let rotated = block.map(([r, c]) => [c, -r]);
    
    // 2. 다시 (0,0) 기준으로 정규화 (blockmove 재활용)
    return blockmove(rotated, Infinity); 
}

// 비교를 위한 정렬 헬퍼 함수
const sortBlock = (block) => {
    return block.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
};

function solution(game_board, table) {
    let answer = 0;
    
    let blanks = [];
    let blocks = [];
    
    // 1. 빈공간 찾기 -> bfs
    // 2. 블록 찾기 -> bfs
    // 3. 블록 맞춰넣기 -> 움직이기와 돌리기
    
    // 빈공간 찾기
    for (let i=0; i<game_board.length; i++){
        for(let j=0; j<game_board.length; j++){
            if(game_board[i][j] === 0){
                blanks.push(bfs([[i,j]], game_board, 1));
            }
        }
    }
    
    // 블록 찾기
    for (let i=0; i<table.length; i++){
        for(let j=0; j<table.length; j++){
            if(table[i][j] === 1){
                blocks.push(bfs([[i,j]], table, 0));
            }
        }
    }
    
    blocks.forEach((val)=>{
        for (let i = 0; i < blanks.length; i++){
            let temp = false;

            // 블록과 빈칸의 크기가 다르면 비교할 필요 없음 (성능 최적화)
            if (val.length !== blanks[i].length) continue;
            
            let rotatedVal = val;
            for (let j = 0; j< 4; j++){
                rotatedVal = rotate(rotatedVal);

                if (JSON.stringify(sortBlock([...rotatedVal])) === JSON.stringify(sortBlock([...blanks[i]]))){
                    blanks.splice(i,1);
                    answer += val.length;
                    temp = true;
                    break;
                }
            }
            if(temp) break;
        }
    });
    
    
    return answer;
}
