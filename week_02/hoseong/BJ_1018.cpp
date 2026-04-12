#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<string> board(N);
    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    int result = 64; // 최대 8x8 전부 바꾸는 경우

    // 모든 8x8 시작점 탐색
    for (int x = 0; x <= N - 8; x++) {
        for (int y = 0; y <= M - 8; y++) {

            int countW = 0; // 시작이 W
            int countB = 0; // 시작이 B

            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {

                    // 현재 위치 실제 색
                    char current = board[x + i][y + j];

                    // (i + j) 짝/홀에 따라 기대 색 결정
                    if ((i + j) % 2 == 0) {
                        if (current != 'W') countW++;
                        if (current != 'B') countB++;
                    } else {
                        if (current != 'B') countW++;
                        if (current != 'W') countB++;
                    }
                }
            }

            result = min(result, min(countW, countB));
        }
    }

    cout << result << endl;
    return 0;
}

/*
[풀이 전략]

- 8×8 크기의 모든 부분 보드를 브루트포스로 탐색
- 각 영역마다 두 가지 경우를 비교
  1. 시작 색이 'W'인 경우
  2. 시작 색이 'B'인 경우
- 두 경우 중 다시 칠해야 하는 최소 횟수를 선택

---

[핵심 아이디어]

- 체스판 규칙:
  (i + j) % 2 == 0 → 시작 색
  (i + j) % 2 == 1 → 반대 색

- 현재 색과 기대 색이 다르면 카운트 증가

---

[시간 복잡도]

O((N - 7) × (M - 7) × 8 × 8)
≈ O(N × M × 64)
≈ O(N × M)

- N, M ≤ 50
→ 최대 연산량: 43 × 43 × 64 = 118336

※ 시작 색 2가지(W/B)는 상수이므로 Big-O에서 생략 가능

→ 충분히 브루트포스로 해결 가능

---

[정리]

- 완전탐색 + 구현 문제
- 핵심은 "두 가지 시작 색을 모두 비교하는 것"
*/