from itertools import combinations
import math

def solution(nums):
    answer = 0
    combList = list(map(sum,list(combinations(nums,3))))  
    
    for comb in combList:
        #소수인지 여부 판별
        for i in range(2,math.ceil(comb)):
            if comb%i == 0:
                break
        else: 
            answer += 1
        
    return answer
