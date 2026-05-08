def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera = -30001

    for start, end in routes:
        if start > camera:
            answer += 1
            camera = end

    return answer