def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idx = { e : i for i , e in enumerate(enroll)}
    
    for s, a in zip(seller,amount):
        cur = s
        money = a * 100
        while cur != '-':
            if money == 0: # 효율성을 위한 중요한 코드!!!!
                break
            tip = money // 10
            answer[idx[cur]] += (money - tip)
            money = tip
            cur = referral[idx[cur]]
        
    return answer
