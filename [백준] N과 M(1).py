
def solution(n,m):
    global visited, cnt, total
    total, cnt = n, m
    visited = []
    for i in range(1,n+1):
        backtracking(i,1)
        


def backtracking(j,k):
    global visited, cnt, total
    visited.append(j)
    if k == cnt:
        for num in visited:
            print(num,end=' ')
        print() #줄바꿈
        visited.pop()
        return

    for i in range(1,total+1):
        if i not in visited:
            backtracking(i,k+1)
    visited.pop()
