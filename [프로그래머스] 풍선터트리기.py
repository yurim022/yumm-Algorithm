def solution(a):
    #왼쪽이나 오른쪽에 나보다 큰수만 있으면 최후에 남을 수 있음
    result = [False for _ in a]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)
