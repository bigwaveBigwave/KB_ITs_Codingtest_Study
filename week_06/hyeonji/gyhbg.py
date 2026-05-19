def solution(id_list, report, k):

    # 각 유저가 신고한 사람 저장 (set 사용)
    report_dict = {}

    for user in id_list:
        report_dict[user] = set()

    # 신고 기록 저장
    for r in report:
        reporter, reported = r.split()

        report_dict[reporter].add(reported)

    # 신고당한 횟수 저장
    reported_count = {}

    for user in id_list:
        reported_count[user] = 0

    # 신고당한 횟수 계산
    for reporter in report_dict:

        for reported in report_dict[reporter]:
            reported_count[reported] += 1

    # 메일 계산
    answer = []

    for user in id_list:

        mail = 0

        for reported in report_dict[user]:

            if reported_count[reported] >= k:
                mail += 1

        answer.append(mail)

    return answer