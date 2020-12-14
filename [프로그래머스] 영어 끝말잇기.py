import math

def solution(n, words):
    answer = [0,0]
    told = [] #이미 말한 단어
    seq = 0 #말한 순서
    lastWord = ''
    for word in words:
        seq +=1
        if word in told or not word.startswith(lastWord):
            answer[0], answer[1] = seq%n if not seq%n==0 else n, math.ceil(seq/n)
            break
        told.append(word)
        lastWord = word[-1]

    return answer
