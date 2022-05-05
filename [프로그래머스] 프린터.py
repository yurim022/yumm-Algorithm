from collections import deque
def solution(priorities, location):
    answer = 0
    priQue = deque([(p,e) for e,p in enumerate(priorities)])
    while priQue:
        element = priQue.popleft()
        if priQue and element[0] < max(priQue)[0]: #우선순위가 가장 높지 않으면
            priQue.append(element)#꺼내서 다시 맨 뒤로
        else:
            answer += 1 #꺼내어질때마다 +1
            if element[1] == location:
                return answer

            
            
---------------------------------------------------
            
#2022-05-06 다시 풀기
from collections import deque
def solution(priorities, location):
    p = deque([ (i, priority) for i, priority in enumerate(priorities)])
    answer = 0
    
    while len(p) > 0:
        max_priority = maxValue(p) #pop 하기 전에 max 값 알아야 함 주의!
        (nowLoc, nowP) = p.popleft()
        if nowP == max_priority:
            answer += 1 #출력
            if nowLoc == location:
                return answer
        else: #가장 높은 우선순위가 아니면 뒤로 보냄
            p.append((nowLoc,nowP))
    
    return 0


def maxValue(priorities):
    maxP = 0
    for (i,p) in priorities:
        if p > maxP :
            maxP =  p
    return maxP
