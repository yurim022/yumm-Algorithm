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


#다른분 풀이
#index 0부터 시작하면 더 깔끔하게 정리 가능
#python indexing으로 별개의 변수 선언하지 않고 바로 처리
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
