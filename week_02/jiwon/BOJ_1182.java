package week_02.jiwon;

import java.util.Scanner;

public class BOJ_1182 {

    static int N, S;
    static int[] arr;
    static int count = 0;

    public static void main(String[] args) {
        // 입력받기
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = sc.nextInt();
        arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // DFS 시작
        dfs(0, 0);

        // S가 0인 경우 : 공집합인 경우 제외하기
        if(S == 0) {
            System.out.println(count - 1);
        } else {
            System.out.println(count);
        }
    }

    public static void dfs(int idx, int sum) {
        // 종료 조건 : 모든 숫자 확인한 경우
        if(idx == N) {
            if(sum == S){
                count++;
            }
            return;
        }

        // 1) 현재 숫자 포함하는 경우 : sum에 현재 숫자 더하기
        dfs(idx + 1, sum + arr[idx]);

        // 2) 현재 숫자 포함하지 않는 경우 : sum 유지
        dfs(idx + 1, sum);
    }
}