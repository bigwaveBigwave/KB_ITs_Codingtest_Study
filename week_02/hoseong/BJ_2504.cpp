#include <iostream>
#include <stack>
using namespace std;

int main() {
    string s;
    cin >> s;

    stack<char> st;
    int result = 0;
    int temp = 1;

    for (int i = 0; i < s.length(); i++) {
        char c = s[i];

        // 여는 괄호
        if (c == '(') {
            temp *= 2;
            st.push(c);
        }
        else if (c == '[') {
            temp *= 3;
            st.push(c);
        }
        // 닫는 괄호
        else if (c == ')') {
            // 유효성 검사
            if (st.empty() || st.top() != '(') {
                cout << 0 << endl;
                return 0;
            }

            // 바로 닫히는 경우
            if (s[i - 1] == '(') {
                result += temp;
            }

            st.pop();
            temp /= 2;
        }
        else if (c == ']') {
            // 유효성 검사
            if (st.empty() || st.top() != '[') {
                cout << 0 << endl;
                return 0;
            }

            // 바로 닫히는 경우
            if (s[i - 1] == '[') {
                result += temp;
            }

            st.pop();
            temp /= 3;
        }
    }

    // 스택이 비어있지 않으면 잘못된 괄호열
    if (!st.empty()) {
        cout << 0 << endl;
    } else {
        cout << result << endl;
    }

    return 0;
}


/*
[풀이 전략]
숫자가 들어오는게 아니라 괄호의 depth로 곱연산 합연산이 분리되는 문제

- 스택을 이용하여 괄호의 유효성 검사와 값을 동시에 처리
- 여는 괄호를 만나면 스택에 push하고, temp(곱셈 값)를 증가
- 닫는 괄호를 만나면:
  1. 올바른 짝인지 확인 (유효성 검사)
  2. 바로 닫히는 구조라면 result에 temp 더하기
  3. 이후 temp를 나누어 원상 복구

---

[핵심 아이디어]

- 괄호 값 규칙
  () = 2, [] = 3
  (X) = 2 * X
  [X] = 3 * X
  XY = X + Y

- temp: 현재 괄호 깊이에 따른 누적 곱
  '(' → temp *= 2
  '[' → temp *= 3

- 닫는 괄호 처리
  - 직전 문자가 여는 괄호라면 (즉, 바로 닫힘)
    → result += temp

  - 이후 temp를 나누어 이전 상태로 복귀

---

[시간 복잡도]

O(N)
- 문자열을 한 번만 순회
- N ≤ 30 → 매우 빠름

---

[정리]

- 스택으로 괄호의 짝을 확인하면서 동시에 값 계산
- 핵심은 "temp를 이용한 누적 곱"과 "즉시 닫힘 판단"
- 유효하지 않은 괄호열이면 즉시 0 출력
*/