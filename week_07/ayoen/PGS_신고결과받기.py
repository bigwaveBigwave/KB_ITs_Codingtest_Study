def solution(id_list, report, k):
    # 1. 중복 신고 제거(set을 이용하면 똑같은 신고는 하나만 남음)
    report = set(report)

    # 2. 필요한 장부들 초기화
    report_counts = {x : 0 for x in id_list}
    user_reports = {x:[] for x in id_list}

    #3 신고 정보분석
    for r in report:
        reporter, reported = r.split()
        report_counts[reported] += 1
        user_reports[reporter].append(reported)

        # 4. 메일 받을 횟수 계산
        answer = []
        for user in id_list:
            mail_count = 0
            for reported_user in user_reports[user]:
                if report_counts[reported_user] >= k:
                    mail_count += 1
            answer.append(mail_count)
    return answer