
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



#2. stack에 index를 넣어준다.
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
