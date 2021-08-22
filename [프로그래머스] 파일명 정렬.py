import re

def solution(files):
    l = [f for f in enumerate(files)]
    l.sort(key = lambda x:(re.findall('^[a-zA-Z]{1}[a-zA-z .-]*',x[1])[0].lower(),
               re.findall('[0-9]+',x[1])[0].zfill(5),
               x[0]))
    answer = [ e for i,e in l]
    return answer
