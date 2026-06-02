import java.util.*;

class pg_퍼즐조각채우기 {
    int [] dr = {-1,1,0,0}; //상,하,좌,우
    int [] dc = {0,0,-1,1};

    //좌표만 담는 함수
    class Point {
        int r, c;
        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    // 좌표 줄 세우기
    private void sortPiece(List<Point> piece) {
        Collections.sort(piece, (p1, p2) -> {
            if(p1.r != p2.r) return p1.r - p2.r; //위아래
            return p1.c - p2.c; //좌우
        });
    }

    //모든 좌표의 시작점을 0,0으로
    private List<Point> normalize(List<Point> piece) {
        int minR = Integer.MAX_VALUE;
        int minC = Integer.MAX_VALUE;

        //가장 작은 값 찾기
        for (Point p : piece){
            minR = Math.min(minR, p.r);
            minC = Math.min(minC, p.c);
        }

        //최솟값만큼 빼서 0,0 맞추기
        List<Point> result = new ArrayList<>();
        for (Point p : piece) {
            result.add(new Point(p.r - minR, p.c - minC));
        }

        sortPiece(result);
        return result;
    }

    //90도 회전시키기
    private List<Point> rotate(List<Point> piece) {
        List<Point> rotated = new ArrayList<>();
        for (Point p : piece) {
            rotated.add(new Point(p.c, -p.r));
        }
        return normalize(rotated);
    }

    // 두조각이 똑같은지 확인하기
    private boolean isSameShape(List<Point> a, List<Point> b) {
        //길이가 다르면 다른 조각
        if(a.size() != b.size())
            return false;

        //하나씩 꺼내서 좌표가 같은지 확인
        for (int i = 0; i<a.size(); i++) {
            if (a.get(i).r != b.get(i).r || a.get(i).c != b.get(i).c) {
                return false;
            }
        }
        return true;
    }

    private List<Point> bfs(int[][] board, boolean[][] visited, int r, int c, int target) {
        List<Point> piece = new ArrayList<>();
        Queue<Point> q = new LinkedList<>();

        q.add(new Point(r, c));
        visited[r][c] = true;

        while (!q.isEmpty()) {
            Point curr = q.poll();
            piece.add(curr);

            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if (nr >= 0 && nr < board.length && nc >= 0 && nc < board.length
                        && !visited[nr][nc] && board[nr][nc] == target) {
                    visited[nr][nc] = true;
                    q.add(new Point(nr, nc));
                }
            }
        }
        return normalize(piece); //정규화해서 넘겨줌
    }

    public int solution(int[][] game_board, int[][] table) {
        int n = game_board.length;

        List<List<Point>> emptySpaces = new ArrayList<>();
        List<List<Point>> puzzles = new ArrayList<>();
        boolean[][] vBoard = new boolean[n][n];
        boolean[][] vTable = new boolean[n][n];

        // 보드 전체를 돌며 빈공간(0)과 퍼즐(1) 캐내기
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(game_board[i][j] == 0 && !vBoard[i][j]){
                    emptySpaces.add(bfs(game_board, vBoard, i, j,0));
                }
                if(table[i][j] == 1 && !vTable[i][j]) {
                    puzzles.add(bfs(table, vTable, i, j, 1));
                }
            }
        }

        int answer = 0;
        boolean[] used = new boolean[puzzles.size()];

        //빈공간에 퍼즐 맞춰보기
        for (List<Point> space : emptySpaces) {
            for (int i = 0; i < puzzles.size(); i++) {
                if(used[i] || space.size() != puzzles.get(i).size()) continue;
                List<Point> p = puzzles.get(i);
                boolean matched = false;

                //4방향으로 돌리며 확인
                for (int rot = 0; rot < 4; rot++) {
                    if(isSameShape(space, p)) {
                        matched = true;
                        break;
                    }
                    p = rotate(p); //안맞으면 회전
                }
                if(matched) {//맞았다면
                    answer += space.size(); //점수 추가
                    used[i] = true; //사용완료 표시
                    break;
                }
            }
        }
        return answer;
    }
}