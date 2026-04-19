class Targetnumber {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        answer += casefunc(numbers, target, 0, '+', 0) + casefunc(numbers, target, 0, '-', 0);
        return answer;
    }

    public int casefunc(int[] numbers, int target, int idx, char mark, int sum) {
        if (mark == '+') {
            sum += numbers[idx];
        } else {
            sum -= numbers[idx];
        }

        if (idx == numbers.length-1) {
            if (sum == target) {
                return 1;
            } else {
                return 0;
            }
        } else {
            return casefunc(numbers, target, idx+1, '+', sum) + casefunc(numbers, target, idx+1, '-', sum);
        }
    }
}