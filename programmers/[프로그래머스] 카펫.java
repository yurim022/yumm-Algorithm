package programmers;

import java.lang.*;

class Solution {
    public int[] solution(int brown, int red) {
        int mul = brown +red;
        for(int i = 3; i<= Math.sqrt(mul); i++){
            if(mul%i == 0){
                int col = i; //세로
                int row = mul/i; //가로
                if(((row+col)*2-4) == brown){
                    int[] answer = new int[2];
                    answer[0] = row;
                    answer[1] = col;
                    return answer;
                }
            }
        }
        
        int[] nop = new int[2];
        nop[0] = 0;
        nop[1] = 0;
        return nop; 

    }
}
