import java.io.*;
import java.util.*;

public class bj_1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //문자열 받아오기

        StringTokenizer st = new StringTokenizer(br.readLine()); //공백있는 문자열을 쪼개기
        int N = Integer.parseInt(st.nextToken());//문자열로 받은것을 숫자로 변환
        int M = Integer.parseInt(st.nextToken());

        char[][] board = new char[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine(); //공백없는 문자열 받기
            for (int j = 0; j < M; j++) {
                board[i][j] = line.charAt(j);
                //charAt() : string로 받은 문자열을 한글자만 선택해서 char로 받기
            }
        }

        int min = 64;//다시 칠할 갯수의 최댓값
        for (int i = 0; i<=N-8; i++){
            for (int j = 0; j <= M-8; j++){
                int count = getCount(i, j, board);
                if(count<min){
                    min = count;
                }
            }
        }
        System.out.println(min);

    }
    public static int getCount(int x, int y, char[][] board){
        int count = 0;

        for (int i = x; i < x + 8; i++) {
            for (int j = y; j < y + 8; j++) {
                boolean isEven = (i + j) % 2 == 0;

                if (isEven) {
                    if (board[i][j] != 'W') count++;
                } else {
                    if (board[i][j] != 'B') count++;
                }
            }
        }
        return Math.min(count, 64 - count);
    }
}
