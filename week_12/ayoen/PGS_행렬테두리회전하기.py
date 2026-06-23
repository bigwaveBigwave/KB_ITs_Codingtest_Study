def solution(rows, columns, queries):
    board = [[i * columns + j + 1 for j in range(columns)]
             for i in range(rows)]

    answer = []

    for x1, y1, x2, y2 in queries:

        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        nums = []

        # 위
        for y in range(y1, y2):
            nums.append(board[x1][y])

        # 오른쪽
        for x in range(x1, x2):
            nums.append(board[x][y2])

        # 아래
        for y in range(y2, y1, -1):
            nums.append(board[x2][y])

        # 왼쪽
        for x in range(x2, x1, -1):
            nums.append(board[x][y1])

        answer.append(min(nums))

        nums = [nums[-1]] + nums[:-1]

        idx = 0

        # 위
        for y in range(y1, y2):
            board[x1][y] = nums[idx]
            idx += 1

        # 오른쪽
        for x in range(x1, x2):
            board[x][y2] = nums[idx]
            idx += 1

        # 아래
        for y in range(y2, y1, -1):
            board[x2][y] = nums[idx]
            idx += 1

        # 왼쪽
        for x in range(x2, x1, -1):
            board[x][y1] = nums[idx]
            idx += 1

    return answer