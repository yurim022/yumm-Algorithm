package programmers;

import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

class Solution{
    public String solution(String[] participant, String[] completion){
        Map<String,Integer> find = new HashMap<>();
        for (String part: participant) find.put(part,find.getOrDefault(part,0)+1);
        for (String comp: completion) find.put(comp,find.get(comp)-1);
        for (String key : find.keySet()) 
            if (find.get(key) != 0) return key;
        return "None";
    }    
}
