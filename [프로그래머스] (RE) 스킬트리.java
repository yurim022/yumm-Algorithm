import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        ArrayList<String> trees = new ArrayList<String>(Arrays.asList(skill_trees));
        Iterator<String> iter = trees.iterator();
        
        while(iter.hasNext()){
            if(skill.indexOf(iter.next().replaceAll("[^"+skill+"]",""))!= 0){
                iter.remove();
            }
        }
        
        return trees.size();
    }
}
