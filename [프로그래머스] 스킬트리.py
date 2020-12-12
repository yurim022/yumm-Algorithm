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
