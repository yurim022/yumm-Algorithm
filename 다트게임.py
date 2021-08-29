def solution(dartResult):
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    answer =[]

    sdt = ['S','D','T']
    i = -1
    
    for j in point:
        if j in sdt:
            answer[i] = answer[i]**(sdt.index(j)+1)
        elif j == '*':
            answer[i] *= 2
            if i>0:
                answer[i-1] *= 2
        elif j == '#' :
            answer [i] *= -1
        else:
            answer.append(int(j))
            i += 1


    return sum(answer)


----

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
