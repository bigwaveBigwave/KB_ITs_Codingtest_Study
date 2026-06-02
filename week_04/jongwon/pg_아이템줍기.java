import java.util.LinkedList;
import java.util.Queue;
import java.util.*;

class pg_아이템줍기 {
    int [][] map = new int [102][102]; //맵을 2배로
    int [] dx = {-1,1,0,0};
    int [] dy = {0,0,-1,1};

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        for (int[] rect : rectangle) {
            int x1 = rect[0]*2;
            int x2 = rect[2]*2;
            int y1 = rect[1]*2;
            int y2 = rect[3]*2;

            for(int i = x1; i <= x2; i++){
                for(int j = y1; j <= y2; j++){
                    if(map[i][j] == -1) //사각형 내부(이미 겹쳐져있는곳)
                        continue;
                    if (i > x1 && i < x2 && j > y1 && j < y2) {
                        map[i][j] = -1;// 내부 -1
                    }else {
                        map[i][j] = 1;//테두리
                    }
                }
            }
        }

        return bfs(characterX *2, characterY*2, itemX*2, itemY*2);
    }

    public int bfs(int startX, int startY, int targetX, int targetY) {
        Queue<int[]> q = new LinkedList<>();
        //x좌표, y좌표, 이동거리를 담음
        q.offer(new int[]{startX, startY, 0});

        boolean[][] visited = new boolean[102][102];
        visited[startX][startY] = true;

        while(!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            int dist = curr[2];

            //목적지에 도착했다면
            if(x == targetX && y == targetY) {
                return dist/2; // 맨처음에 2배를 해줬기에 다시 나눠줌
            }

            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < 102 && ny >= 0 && ny < 102) {
                    if(!visited[nx][ny] && map[nx][ny] == 1) {
                        visited[nx][ny] = true;
                        q.offer(new int[]{nx, ny, dist + 1});
                    }
                }
            }
        }
        return 0;
    }
}