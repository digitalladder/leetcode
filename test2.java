import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
public class Main{
  public static void main(String[] args){
    Scanner in=new Scanner(System.in);
    int t = in.nextInt();
    for (int i=0;i<t;i++){
        int n = in.nextInt();
        int k = in.nextInt();
        ArrayList<Integer> inform = new ArrayList<>();
        for(int j=0;j<k;j++){
            inform.add(in.nextInt());
        }
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int c=1;c<n+1;c++) {
            adjList.put(c, new ArrayList<Integer>());
        }
        int m = in.nextInt();
        for (int l=0;k<m;k++){
            int a = in.nextInt();
            int b = in.nextInt();
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }
        System.out.println(adjList);
    }
  }
}