#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> sequence(n);
    for (int i = 0; i < n; i++) {
        cin >> sequence[i];
    }

    stack<int> s;
    vector<char> operations;
    int current = 1; // 스택에 넣을 수

    for (int i = 0; i < n; i++) {
        int target = sequence[i];

        // target까지 오름차순으로 push
        while (current <= target) {
            s.push(current++);
            operations.push_back('+');
        }

        // 스택 top이 원하는 값과 다르면 불가능
        if (s.top() == target) {
            s.pop();
            operations.push_back('-');
        } else {
            cout << "NO\n";
            return 0;
        }
    }

    // 연산 출력
    for (char op : operations) {
        cout << op << "\n";
    }

    return 0;
}

/*
current는 1부터 n까지 차례대로 스택에 넣는 수를 의미
주어진 수열 sequence[i]가 나올 때까지 스택에 push(+)를 반복
스택의 top이 sequence[i]와 같으면 pop(-)을 수행
top이 다르면 수열을 만들 수 없으므로 "NO" 출력 후 종료
*/