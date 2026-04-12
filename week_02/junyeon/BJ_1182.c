#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int N = 0;
int S = 0;
int cnt = 0;
int numArr[21];
void compute(int idx, int sum) {
	if (idx == N) {
		return;
	}
	if (sum + numArr[idx] == S) { cnt++; }

	compute(idx + 1, sum);

	compute(idx + 1, sum + numArr[idx]);

}


int main(void) {
	scanf("%d %d", &N, &S);
	int sum = 0;
	int result = 0;
	for (int i = 0; i < N; i++) {
		int temp;
		scanf("%d", &temp);
		numArr[i] = temp;
	}
	compute(0, 0);
	printf("%d", cnt);

}