import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
       
        for(int i = 0; i < bridge_length; i++){
            q.add(0);
        }
       int idx = 0;
        while(!q.isEmpty()){
            q.poll();
            answer++;
            if(idx <= truck_weights.length-1){
                if(weight >= (sumOfQ(q) + truck_weights[idx])){
                    q.add(truck_weights[idx]);
                    idx++;
                }else{
                    q.add(0);
                }
            }
        }
        
        
        return answer;
    }
    
    public static int sumOfQ(Queue<Integer> q){
        return q.stream().reduce(0,Integer::sum);
    }
}
