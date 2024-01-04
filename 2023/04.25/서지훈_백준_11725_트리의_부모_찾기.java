import java.io.*;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] adjacent;
    static int[] parent;
    static boolean[] visited;
    public static void dfs(int node){
        for(Integer next_node : adjacent[node]){
            if(!visited[next_node]){
                visited[next_node] = true;
                parent[next_node] = node;
                dfs(next_node);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        adjacent = new ArrayList[N+1];
        for(int i = 1; i <= N; ++i){
            adjacent[i] = new ArrayList<>();
        }

        for(int i = 0; i < N-1; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            adjacent[a].add(b);
            adjacent[b].add(a);
        }

        parent = new int[N+1];
        visited = new boolean[N+1];
        visited[1] = true;
        dfs(1);

        for(int i = 2; i <= N; ++i){
            bw.write(Integer.toString(parent[i]));
            bw.write("\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
