#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int checkArr(int x, int y, char checkedArr[51][51]) {
	char w_first[9][9] = { {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'} };
	char b_first[9][9] = { {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'}, {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}, {'W', 'B', 'W', 'B','W', 'B','W', 'B'} };

	int cnt_w = 0;
	int cnt_b = 0;

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (w_first[i][j] != checkedArr[x + i][y + j]) {
				cnt_w++;
			}
		}
	}
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (b_first[i][j] != checkedArr[x + i][y + j]) {
				cnt_b++;
			}
		}
	}

	return cnt_w < cnt_b ? cnt_w : cnt_b;


}

int main(void) {
	int N;
	int M;
	scanf("%d %d", &N, &M);
	int min = 64;
	char arr[51][51];

	for (int i = 0; i < N; i++) {
		char str[51];
		scanf("%s", str);
		strcpy(arr[i], str);
	}



	for (int i = 0; i <= N - 8; i++) {
		for (int j = 0; j <= M - 8; j++) {
			int checkResult = checkArr(i, j, arr);
			min = min < checkResult ? min : checkResult;
		}
	}
	printf("%d", min);
}