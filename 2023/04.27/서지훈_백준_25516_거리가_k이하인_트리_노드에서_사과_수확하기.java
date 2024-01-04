import java.io.*;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] adjacent;
    static boolean[] visited;
    static int[] apples;
    static int k, result;
    public static void dfs(int node, int distance){
        if(k > distance){
            for(Integer next_node : adjacent[node]){
                if(!visited[next_node]){
                    visited[next_node] = true;
                    result += apples[next_node];
                    dfs(next_node, distance+1);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        adjacent = new ArrayList[n];
        for(int i = 0; i < n; ++i){
            adjacent[i] = new ArrayList<>();
        }

        for(int i = 0; i < n-1; ++i){
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            adjacent[p].add(c);
            adjacent[c].add(p);
        }

        apples = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; ++i){
            apples[i] = Integer.parseInt(st.nextToken());
        }


        visited = new boolean[n];
        visited[0] = true;

        result = apples[0];
        dfs(0, 0);

        bw.write(Integer.toString(result));

        bw.flush();
        bw.close();
        br.close();
    }
}