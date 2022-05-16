from collections import Counter

def solution(id_list, report, k):
    report_user = dict()
    for id_ in id_list:
        report_user[id_] = set()
    
    for r in report:
        er, ed = r.split(' ')
        report_user[er].add(ed)
    
    reported = []
    for users in report_user.values():
        reported.extend(users)
    
    stopped = [ key for key, value in Counter(reported).items() if value >= k ]
    
    answer = []
    for users in report_user.values():
        cnt = 0
        for user in users:
            if user in stopped:
                cnt += 1
        answer.append(cnt)
    return answer
