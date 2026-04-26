#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int>& numbers, int target, int index, int sum) {
    // 모든 숫자를 다 사용한 경우
    if (index == numbers.size()) {
        if (sum == target) {
            answer++;
        }
        return;
    }

    // 현재 숫자를 더하는 경우
    dfs(numbers, target, index + 1, sum + numbers[index]);

    // 현재 숫자를 빼는 경우
    dfs(numbers, target, index + 1, sum - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}
