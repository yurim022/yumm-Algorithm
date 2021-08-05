
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds)     {
        Stack<Integer> stack = new Stack<Integer>();
        Queue<Integer> answerQ = new LinkedList<>();
        
        for(int i = progresses.length -1; i >=0; i--)
            stack.add((100 - progresses[i])/speeds[i] + 
                      (((100 - progresses[i])%speeds[i]) == 0 ? 0 : 1));
        
        while(!stack.isEmpty()){
            int count = 1;
            int top = stack.pop();
            
            while(!stack.isEmpty() && stack.peek() <= top){
                count++;
                stack.pop();
            }
            
            answerQ.add(count);
        }
        
        int[] answer = new int[answerQ.size()];
        for(int idx = 0; idx< answer.length; idx++){
            answer[idx] = answerQ.poll();
        }
        
        return answer;
 
    }
}
