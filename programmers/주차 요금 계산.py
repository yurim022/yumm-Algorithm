from collections import defaultdict
import math

def solution(fees, records):
    def toMinute(time):
        hour, minute = time.split(':')
        return int(hour)* 60 + int(minute)
    def calculateFee(minute):
        if minute <= defaultMin:
            return defaultCost
        return defaultCost + math.ceil((minute - defaultMin) / unitMin)* unitCost
        
    defaultMin, defaultCost, unitMin, unitCost = fees
    ins = defaultdict(int)
    accumulates = defaultdict(int)
    
    for record in records:
        time, carNum, status = record.split(' ')
        if status == 'IN':
            ins[carNum] = toMinute(time)
            
        if status == 'OUT':
            outTime = toMinute(time)
            inTime = ins[carNum]
            accumulates[carNum] += (outTime - inTime)
            ins.pop(carNum)
    
    for key in  ins.keys():
        outTime = toMinute('23:59')
        inTime = ins[key]
        accumulates[key] += (outTime - inTime)
        
        
    answer = [ calculateFee(item[1]) for item in sorted(accumulates.items(), key = lambda x: x[0])]   
    return answer
