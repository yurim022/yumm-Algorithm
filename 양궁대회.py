#### copy.deepcopy 필수!!!

import copy

maxScoreDiff = 0
maxCandidate = []
def solution(n, info):
    global maxScoreDiff,maxCandidate
    def findWin(apacheScore,lionScore,targetScore,remain,candidate):
        global maxScoreDiff,maxCandidate
        if targetScore == 0:
            temp = copy.deepcopy(candidate)
            if remain:
                temp[10] = remain
                
            if lionScore > apacheScore: #라이언이 어피치를 이겼으면
                difference = (lionScore-apacheScore)
                if difference > maxScoreDiff:
                    maxScoreDiff = difference
                    maxCandidate = [temp]
                    
                if difference == maxScoreDiff:
                    maxCandidate.append(temp)
            return
        
        #어피치보다 1크거나
        cnt = info[10-targetScore] + 1
        if cnt <= remain:
            candidate[10-targetScore] = cnt
            findWin(apacheScore,lionScore+targetScore,targetScore -1,remain-cnt,candidate)
            candidate[10-targetScore] = 0
        
        #0
        if info[10-targetScore] == 0 :#둘다 0
            findWin(apacheScore,lionScore,targetScore-1,remain,candidate)
        else: #어피치가 점수 가져가고 라이언 0
            findWin(apacheScore+targetScore,lionScore,targetScore-1,remain,candidate)        

        
    findWin(0,0,10,n,[0]*11)
    if len(maxCandidate) == 0:
        return [-1]
    maxCandidate.sort(key = lambda x:x[::-1],reverse=True)
    return maxCandidate[0]
