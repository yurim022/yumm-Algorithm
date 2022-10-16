##첫번째 풀이

import re

def solution(files):
    l = [f for f in enumerate(files)]
    l.sort(key = lambda x:(re.findall('^[a-zA-Z]{1}[a-zA-z .-]*',x[1])[0].lower(),
               re.findall('[0-9]+',x[1])[0].zfill(5),
               x[0]))
    answer = [ e for i,e in l]
    return answer


##두번째 풀이 불필요한 enumerate 과정과, 원래 순서를 유지하는 쏘팅 제외
import re

def solution(files):
    files.sort(key = lambda file:(re.findall('^[a-zA-Z]{1}[a-zA-z .-]*',file)[0].lower(),
               re.findall('[0-9]+',file)[0].zfill(5)))
    return files

