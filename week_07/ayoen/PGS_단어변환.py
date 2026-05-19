from collections import deque

def solution(begin, target, words):
    #1. target이 words에 없으면 절대 변환 불가
    if target not in words:
        return 0

    queue = deque([(begin, 0)]) #현재 단어, 이동단계
    visited = set() # 이미 방문한 단어 체크

    while queue:
        current_word, step = queue.popleft()

        # 목표 단어에 도달하면 즉시 종료
        if current_word == target:
            return step

        for word in words:
            # 아직 방문 안 했고 한글자만 다르다면
            if word not in visited:
                diff_count = 0
                for i in range(len(begin)):
                    if current_word[i] != word[i]:
                        diff_count += 1
                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, step+1))

    return 0
