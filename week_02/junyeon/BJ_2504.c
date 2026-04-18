#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {
	char str[31];
	char stack[31];
	scanf("%s", str);
	int top = -1;
	int temp = 1;
	int sum = 0;
	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '[') {
			temp *= 3;
			stack[++top] = str[i];
		}
		else if (str[i] == '(') {
			temp *= 2;
			stack[++top] = str[i];
		}
		else if (str[i] == ')') {
			if (top != -1 && stack[top] == '(') {
				if (str[i - 1] == '(') {
					sum += temp;
				}
				temp /= 2;
				top--;
			}
			else {
				printf("0");
				return 0;
			}
		}
		else {
			if (top != -1 && stack[top] == '[') {
				if (str[i - 1] == '[') {
					sum += temp;
				}
				temp /= 3;
				top--;
			}
			else {
				printf("0");
				return 0;
			}
		}
	}

	if (top != -1) {
		printf("0");
	}
	else {
		printf("%d", sum);
	}
	return 0;
}