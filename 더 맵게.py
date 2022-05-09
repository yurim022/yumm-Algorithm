import heapq

def solution(scoville, K): #priority que 사용
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
            cnt += 1
        except IndexError:
            return -1
    return cnt


----------------------------------------------------------------

# 2022-05-09 다시품. 위에꺼가 더 

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) <2 :
            return -1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + 2*s2)
        cnt += 1
    
    return cnt
