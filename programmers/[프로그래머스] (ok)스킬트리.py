#내풀이
def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idxs = [tree.index(s) if s in tree else 27 for s in skill]
        flag = True
        for i,j in zip(idxs,idxs[1:]):
            if i>j:
                flag = False
                break
        if flag:
            answer +=1
            
    return answer


##참조할만한 풀이
#python은 for else를 지원한다. 

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer



##참조풀이를 내 식으로 재해석
#deque를 쓰니 더 빠르다
#skill_q = deque(skill) 가 for문안에 들어와야 되는 것 주의
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_q = deque(skill)
        for s in tree:
            if s in skill_q and s != skill_q.popleft():
                break
        else:
            answer +=1
        
    return answer
