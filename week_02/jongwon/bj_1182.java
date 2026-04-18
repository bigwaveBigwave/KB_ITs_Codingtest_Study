import java.io.*;
import java.util.*;

public class bj_1182 {
    static int N, S;
    static int[] arr;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //N과 S를 받아서 그 크기만큼 배열을 만들어서 숫자를 넣음
        StringTokenizer st = new StringTokenizer(br.readLine()); //공백있는 문자열을 쪼개기
        N = Integer.parseInt(st.nextToken());//문자열로 받은것을 숫자로 변환
        S = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());//한 줄 바뀌면 또 선언
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            //배열에 N개의 숫자를 담음
        }

        for(int i = 0; i < N; i++){
            dfs(i, arr[i]);
        }
        System.out.println(count);
    }
    static void dfs(int start, int sum){
        if(sum == S){
            count++;
        }
        for(int next = start+1; next < N; next++){
            dfs(next,sum+arr[next]);
        }
    }
}
