import java.util.ArrayList;
import java.util.HashMap;
class Solution {
    static HashMap<String, Integer> map = new HashMap<String, Integer>();
    static ArrayList<Integer> list = new ArrayList<Integer>();
    static char[] arr;
    static int num = 1;
  public int[] solution(String msg) {

      for(int i = 0;i < 27;i++) map.put(String.valueOf((char)(65+i)), i+1);
      arr = msg.toCharArray();

      while(num <= arr.length) {
            String tmp;
            if(num == arr.length) tmp = "" + arr[num-1];
            else tmp = "" + arr[num - 1] + arr[num];

            encoding(tmp);          
        }
      int[] answer = new int[list.size()];
      int size = 0;
      for(int i : list) {
            answer[size++] = i;
      }


      return answer;
  }
    static void encoding(String tmp) {
        num++;
        if(map.containsKey(tmp) && num < arr.length) {
            encoding(tmp + arr[num]);           
        }
        else if(map.containsKey(tmp)){
            num += 2;
            list.add(map.get(tmp));
        }
        else {
            map.put(tmp, map.size());
            tmp = tmp.substring(0, tmp.length()-1);

            list.add(map.get(tmp));
        }
    }
}
