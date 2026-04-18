#include <iostream>
#include <vector>
using namespace std;

int N, S;
vector<int> arr;
int result = 0;

void dfs(int idx, int sum) {
    // 끝까지 갔을 때
    if (idx == N) {
        if (sum == S) result++;
        return;
    }

    // 현재 원소 선택
    dfs(idx + 1, sum + arr[idx]);

    // 현재 원소 선택 안함
    dfs(idx + 1, sum);
}

int main() {
    cin >> N >> S;

    arr.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    dfs(0, 0);

    // 공집합 제거
    if (S == 0) result--;

    cout << result << endl;
    return 0;
}

/*
[풀이 전략]
DFS를 활용한 부르트포스 (선택 또는 미선택 전부)

- 각 원소를 선택 / 미선택 하는 방식으로 모든 부분수열 탐색
- DFS(백트래킹)를 사용하여 가능한 모든 경우를 탐색
- 부분수열의 합이 S가 되는 경우를 카운트

---

[핵심 아이디어]

- 부분수열의 개수는 총 2^N
- 각 원소마다 두 가지 선택
  1. 선택한다 → sum + arr[idx]
  2. 선택하지 않는다 → 그대로 진행

- DFS 구조
  dfs(idx + 1, sum + arr[idx]); // 선택
  dfs(idx + 1, sum);            // 미선택

- 모든 원소를 확인했을 때 (idx == N)
  → 현재 합이 S와 같으면 count 증가

- 공집합 제외 필요
  → 아무것도 선택하지 않은 경우 sum = 0이 한 번 포함됨
  → S == 0일 경우 결과에서 1 빼기

---

[시간 복잡도]

O(2^N)

- N ≤ 20
→ 최대 약 1,048,576 (약 100만)
→ 완전탐색(브루트포스로 충분히 해결 가능)

---

[정리]

- 전형적인 백트래킹 문제
- 핵심은 "모든 부분수열을 빠짐없이 탐색"하는 것
*/