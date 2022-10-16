# 내풀이

def solution(N, number):
    if N == number:
        return 1

    s = [ set() for x in range(9)] #s[1] -> 사용횟수 1 맞춰주기 위해
    for i in range(1,9):
        s[i].add(int( str(N)*i ))

        
    for target in range(2,9):
        for subSet in range(1,target):
            for op1 in s[subSet]:
                for op2 in s[target-subSet]:
                    s[target].add(op1 - op2)
                    s[target].add(op1 + op2)
                    s[target].add(op1 * op2)
                    if op2 != 0:
                        s[target].add(op1 // op2)
        if number in s[target]:
            return target
        
    
    return -1




-------------------------------------------------------------------------------------------------------------
# 참고한 풀이

def solution(N, number):
    if N == number:
        return 1
        
    # 1. [ SET x 8 ] 초기화. 
    # s[0] -> 연산횟수 = 1, s[1] -> 연산횟수 = 2, ... 
    # s[7] -> N = 8 (s[1] 연산 s[6], s[2] 연산 s[5], s[3] 연산 s[4], ...s[6] 연산 s[1])
    s = [ set() for x in range(8) ] 

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
    #	[{5}, {55}, {555}, {5555} ...]

    # 3. n 일반화
     #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    } 
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer
