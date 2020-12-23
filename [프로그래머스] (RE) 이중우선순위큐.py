import heapq
def solution(operations):
    answer = []
    heapq.heapify(answer)
    
    for operation in operations:
        operator, operand = operation.split()
        operand = int(operand)
        if operator =='I':
            heapq.heappush(answer,operand)
        elif answer:
            if operand > 0:
                answer.remove(max(answer))
            else:
                heapq.heappop(answer)
        
    if not answer: #비어있으면
        return [0,0]
    else:#최대값,최소값
        return [max(answer),answer[0]]
