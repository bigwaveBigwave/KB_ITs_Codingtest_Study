package week_02.jiwon;

import java.util.Scanner;

public class BOJ_1018 {

    public static boolean[][] board;
    public static int min = 64; // 최대 수정 횟수

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        board = new boolean[N][M];

        // 보드 데이터 입력받기
        // W -> true / B -> false 로 저장
        for(int i = 0; i < N; i++) {
            String str = sc.next();
            for(int j = 0; j < M; j++) {
                if(str.charAt(j) == 'W') {
                    board[i][j] = true;
                } else {
                    board[i][j] = false;
                }
            }
        }

        // 모든 시작점 탐색하기
        for(int i = 0; i <= N-8; i++) {
            for(int j = 0; j <= M-8; j++) {
                findMin(i, j);
            }
        }

        System.out.println(min);
    }

    // 시작점 (x, y) 부터 8x8 보드판 검사하는 함수
    public static void findMin(int start_x, int start_y) {
        int end_x = start_x + 8;
        int end_y = start_y + 8;
        int count = 0;

        // 시작점 색깔 기준 
        boolean color = board[start_x][start_y];

        for(int i = start_x; i < end_x; i++) {
            for(int j = start_y; j < end_y; j++) {
                // 현재 칸 색이 예상되는 색과 다르면 count++
                if(board[i][j] != color) {
                    count++;
                }
                color = !color; // 칸 바뀌면 기준 색깔 바뀜 
            }
            color = !color; // 줄 바뀌면 기준 색깔 바뀜
        }
        
        // W로 시작할 때와 B로 시작할 때 중 최솟값 구하기
        count = Math.min(count, 64 - count);
        min = Math.min(min, count);
    }
}