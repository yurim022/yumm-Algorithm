def isCorrect(s):
    #put [,(,{ in stack and pop when ],),} 
    stack = []
    start = ['(','{','[']
    end = [')','}',']']
    for s_ in s:
        if s_ in start:
            stack.append(s_)
            continue
        if len(stack) == 0 :
            stack.append(s_)
            continue
        for i in range(3):
            if s_ == end[i] and stack[-1] != start[i]: return False
        stack.pop() #when s_ is end & s_ == end[i] and stack[-1] == start[i]
    if len(stack) > 0:
        return False
    return True
    
def solution(s):
    answer = 0
    #rotate for n-1
    for i in range(len(s)):
        s = s[1:] + s[0]
        if isCorrect(s):
            answer += 1
    return answer
