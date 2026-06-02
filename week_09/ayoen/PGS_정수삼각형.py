def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            # 맨 왼쪽
            if j == 0:
                triangle[i][j] += triangle[i-1][j]

            # 맨 오른쪽
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]

            # 가운데
            else:
                triangle[i][j] += max(
                    triangle[i-1][j-1],
                    triangle[i-1][j]
                )

    return max(triangle[-1])