def solution(input):
    
    #구현문제
    str_input = str(input)
    str_len = len(str_input)

    #각각 합을 구한다. 
    first = 0
    print(str_len//2)
    for s in str_input[:str_len//2]:
        first += int(s)

    second = 0
    for s in str_input[str_len//2:]:
        second += int(s)

    if first == second:
        print("LUCKY")
    else:
        print("READY")
