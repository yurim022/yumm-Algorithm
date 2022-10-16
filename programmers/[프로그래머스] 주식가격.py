
#1. brute force
def solution(prices):
    #몇초인지
    n = len(prices)
    ans = [0]*n
    for i in range(n):
        for j in range(i+1,n):#만약 0초면 1초부터 비교
            if prices[i] > prices[j]:#주식가격이 떨어지면
                ans[i] += j-i
                break
        else:
            ans[i] = n-i-1
    return ans



--------------------------------------------------

# 2022- 05 -05
# 이게 더 빠름

def solution(prices):
    stack = []
    answer = [ 0 for i in range(len(prices))]
    
    for time, price in enumerate(prices):
        
        if len(stack) > 0:    
            while stack:
                if stack[-1][1] > price:
                    (s_time, s_price) = stack.pop()
                    answer[s_time] = time - s_time
                else: #주식 안떨어졌으면 
                    break
        
        stack.append((time,price))

    
    #끝까지 안떨어진 값들 정리
    cur_time = len(prices) - 1
    while stack:
        (time,price) = stack.pop()
        answer[time] = cur_time - time
        
-----------------------------------------------------
# stack에 index를 넣어준다.
def solution(prices):
    answer = [0]*len(prices)
    stack = []
    #index를 stack에 넣는다.
    
    for i, price in enumerate(prices):
        #stack에 있는 값이 현재값보다 크면 (값이 떨어지면)
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
        
    while stack:
            j = stack.pop()
            answer[j] = len(prices) -1 -j
            
    return answer
