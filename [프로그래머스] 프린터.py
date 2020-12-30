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
