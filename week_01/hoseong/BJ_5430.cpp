#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string p;
        cin >> p;

        int n;
        cin >> n;

        string arr_str;
        cin >> arr_str;

        deque<int> dq;
        string num = "";
        for (char c : arr_str) {
            if (isdigit(c)) num += c;
            else if (c == ',' || c == ']') {
                if (!num.empty()) {
                    dq.push_back(stoi(num));
                    num = "";
                }
            }
        }

        bool reversed = false;
        bool error = false;
        for (char op : p) {
            if (op == 'R') reversed = !reversed;
            else if (op == 'D') {
                if (dq.empty()) {
                    error = true;
                    break;
                }
                if (!reversed) dq.pop_front();
                else dq.pop_back();
            }
        }

        if (error) {
            cout << "error\n";
        } else {
            cout << "[";
            while (!dq.empty()) {
                if (!reversed) {
                    cout << dq.front();
                    dq.pop_front();
                } else {
                    cout << dq.back();
                    dq.pop_back();
                }
                if (!dq.empty()) cout << ",";
            }
            cout << "]\n";
        }
    }

    return 0;
}
/*
- deque 사용: 양쪽에서 제거가 가능하기 때문에 D 연산을 효율적으로 수행할 수 있음.
- reversed 플래그: R이 나올 때마다 뒤집기를 실제로 하지 않고, 뒤집힌 상태인지 여부만 기록.
- D 연산: reversed 상태에 따라 앞(front) 또는 뒤(back)에서 pop.
- 배열 파싱: [1,2,3,4] 같은 입력을 문자열에서 숫자만 추출하여 deque에 저장.
- 출력: 최종 결과를 reversed 상태에 맞게 앞/뒤에서 순차적으로 출력.
*/