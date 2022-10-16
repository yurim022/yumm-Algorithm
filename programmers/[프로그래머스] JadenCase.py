import re

def solution(s):
    answer = s.lower()
    for i in re.findall('^[a-z]|\s[a-z]',answer):
        print(i)
        answer = answer.replace(i,i.upper(),1)
    return answer
