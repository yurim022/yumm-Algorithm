def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    new_board = [[] for i in range(n+1)]
    
    #재배치
    for j in range(n):
            new_board[j+1] = [ board[i][j] for i in range(n-1,-1,-1) if board[i][j] != 0]
    
   # print(new_board)
    #moves에 맞춰서 stack에 넣어주면서 체크
    for moveIdx in moves:
        try:
        	stack.append(new_board[moveIdx].pop())
        	if len(stack) >= 2 and stack[-1]==stack[-2]:
            	 answer += 2
            	 stack = stack[:-2]
        except:
            pass
        #print(f'moveIdx"{moveIdx},new_board:{new_board},stack:{stack}')
    return answer
