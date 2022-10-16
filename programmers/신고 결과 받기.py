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


------
# 인상깊은 풀이

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = { x: 0 for x in id_list}
    
    for r in set(report): # 아예 report 자체를 set...!
        reports[r.split()[1]] += 1
        
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1 # index 함수를 적절하게 

    return answer
