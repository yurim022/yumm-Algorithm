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
