def solution(money):
    #점화식 dp문제
    #table[i] = max(table[i-1], table[i-2] + money[i])
    
    table = [0]*(len(money))
    #첫번째 집을 방문하는 경우
    table[0] = money[0]
    table[1] = table[0]
    for i in range(2, len(money)-1): #circular 조건때문에 나눠주는 것!
        table[i] = max(table[i-1],table[i-2] +money[i])
    answer = max(table) #table[len(money) -1]은 0 이므로 max로 연산
    
    #첫번째 집을 방문하지 않는 경우
    table = [0]*(len(money))
    table[1] = money[1]
    for i in range(2, len(money)):
        table[i] = max(table[i-1],table[i-2] +money[i])
    answer = max(answer, max(table))
    return answer
