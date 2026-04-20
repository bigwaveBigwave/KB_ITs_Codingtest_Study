public class pg_타겟넘버 {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        //index는 몇번째 숫자를 처리하는지를 나타냄
        //sum은 합계
        return answer; //answer는 카운트 한 숫자
    }

    public void dfs(int[] numbers, int target, int index, int sum){
        if(index == numbers.length){// 현재 처리하는 숫자가 마지막까지 가면
            if(sum == target){// 최종 합이 내가 지정한 타겟넘버와 같다면
                answer++; // 카운트를 올려줌
            }
            return;
        }
        //dfs(0,0)부터 시작
        dfs(numbers, target, index + 1, sum+numbers[index]);//더할 때
        dfs(numbers, target, index + 1, sum-numbers[index]);//뺄 때
    }
}
