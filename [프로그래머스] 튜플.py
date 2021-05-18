def solution(s):
    dic = {}
    s = s.replace('{','').replace('}','').split(',');
    #많이 카운트된 원소 순서대로 튜플생성
    for s_ in set(s): 
        dic[s_] = 0
    for s_ in s:
        dic[s_] += 1  #원소의 개수 카운트 
        
    answer = []
    counts = sorted(dic.items(), key = lambda x: x[1],reverse= True) #많이 세어진 순서대로 카운트
    for key, value in counts:
        answer.append(int(key))
    return answer
