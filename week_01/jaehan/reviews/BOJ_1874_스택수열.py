## 스택 수열 Last In First Out


## 예제 입력 1
# 수열 : [4 3 6 8 7 5 2 1]

## 예제 입력 2
# 수열 : [1 2 5 3 4] + - + - + + + - X

# 스택의 top이 현재 필요한 숫자와 다르다면 NO 출력

S = int(input())
my_stack = []
my_arr = []
result = []
count = 1
## 입력 수열 생성
for i in range(S):
    my_arr.append(int(input()))

## 스택 구현 가능성 검증
for target in my_arr:
    while target >= count:
        my_stack.append(count)
        count += 1
        result.append("+")
    if my_stack[-1] == target : 
        my_stack.pop()
        result.append("-")
    else :
        result.append("NO")

if "NO" in result :
    print("NO")
else :
    for r in result:
        print(r)