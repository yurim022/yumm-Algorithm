import java.util.Scanner;
import java.util.StringTokenizer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class printerQueue {

    public static void main(String[] args) throws IOException {


        int numOfTest;
        int numOfDoc;
        int targetDoc;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();

        numOfTest = Integer.parseInt(br.readLine());

        while(numOfTest-- > 0){

            StringTokenizer st = new StringTokenizer(br.readLine());
            numOfDoc = Integer.parseInt(st.nextToken());
            targetDoc = Integer.parseInt(st.nextToken());

            LinkedList<int[]> q = new LinkedList<>(); 
            st = new StringTokenizer(br.readLine());

            for(int i = 0; i <numOfDoc; i++){
                q.offer(new int[] {i, Integer.parseInt(st.nextToken())}); //{initial status, priority}
            }

            int count = 0;

            while(!q.isEmpty()){

                int[] current = q.poll();
                boolean isMax = true;

                //compare priority with remain elements
                for(int i = 0; i < q.size(); i++){

                    if(current[1] < q.get(i)[1]){//current priority is not max

                        q.offer(current); //enqueue current value
                        for(int j = 0; j<i; j++){
                            q.offer(q.poll()); //enqueue left elements
                        }

                        isMax = false;
                        break;

                    }

                }

                if(isMax == false){
                    continue;
                }

                count++;

                //find targetDoc and break 
                if(current[0] == targetDoc){
                    break;
                }
            }

            result.append(count).append('\n');
        }

        br.close();

        //print result
        System.out.println(result);

    }


}
