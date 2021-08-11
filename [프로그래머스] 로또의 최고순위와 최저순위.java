import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int minCorrect = 0;
        int additionalCorrect = 0;

        for(int lotto : lottos){
            for(int win_num : win_nums){
                if(win_num == lotto)
                    minCorrect++;
            }

            if(lotto == 0)
                additionalCorrect++;
        }

        answer[1] = score(minCorrect);
        answer[0] = score(minCorrect + additionalCorrect);

        return answer;
    }

    public int score(int correctCount){
        if(correctCount < 2)
            return 6;
        return 7 - correctCount;
    }
}
