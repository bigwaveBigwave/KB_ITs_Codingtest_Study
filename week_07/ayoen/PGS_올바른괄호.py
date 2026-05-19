def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True