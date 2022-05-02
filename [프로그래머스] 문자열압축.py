def solution(s):
    if(len(s) <3):
        return len(s)
    
    min_len = len(s)
    atom_limit = int(len(s)/2)+1 #압축단위 한계
    for i in range(1,atom_limit):#압축단위 1,2,....limit
        str_compare = s[:i]
        str_list =[]
        str_count =1
        
        for j in range(i,len(s)+1,i): #이 과정을   range 함수로 진행한 것이 굳
            if(str_compare == s[j:j+i]):
                str_count += 1
            else:
                str_list.append("{}".format(str_count if str_count>1 else '')) #+연산자는 메모리 할당을 다시 해줘야 하므로 리스트 사용
                str_list.append(str_compare)
                str_compare = s[j:j+i]
                str_count =1 #다시 1로 
                
        #마지막 비교 문자열을 더해준다
        str_list.append(str_compare)
        final_str =''.join(str_list) #리스트를 문자열로
        if(min_len > len(final_str)):#최소길이 변경
            min_len = len(final_str)            
    
    return 
