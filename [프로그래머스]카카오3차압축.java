import java.util.*;

class Solution {
    public static int[] solution(String msg) {
        ArrayList<Integer> answer = new ArrayList<>();//길이가 유동적이므로 arraylist
        ArrayList<String> dict = new ArrayList<>();
        
        dict.add("0");//index 1부터 시작하기 위해
        char english = 'A';
        //dict 초기설정
        for(int i = 0; i<26;i++){
            dict.add(english++ + "");
        }
        
        //queue에 msg넣어주기 (remove 용이)
        Queue<Character> q = new LinkedList();
        for(int i = 0;i<msg.length();i++){
            q.add(msg.charAt(i));
        }

        while(!q.isEmpty()){
            //사전에 있는지 check
            String w = q.remove()+"";//현재입력 //k
            String next = "";
            if (q.size()>0){
            	next = w+ q.peek();//다음글자 //a
            }
            //사전에 포함하는 데까지 w포함
            boolean flag = false;
            do{
                flag =false;
                    if (dict.contains(next)){//ka
                        flag = true;
                        w  += q.remove(); //kao
                        next = w+q.peek();//q가 비었을 경우 null 반환 
                    }
                    else{
                    	answer.add(dict.indexOf(w));
                        if (!next.equals("")){
                            dict.add(next);
                        }
                    }
            }while (flag);
            
            //사전에 등록
            //다음글자
        }
        
        
        //int[] 로 변환
        int[] returnAns = new int[answer.size()];
        int idx = 0;
        for(int temp :answer){
            returnAns[idx++] = temp;
        }
        
        return returnAns;
    }

}
