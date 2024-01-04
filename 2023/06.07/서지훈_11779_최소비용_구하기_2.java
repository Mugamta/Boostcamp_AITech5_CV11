import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

class Pair{
    private int dest;
    private int weight;
    public Pair(int v, int w){
        this.dest = v;
        this.weight = w;
    }
    public int returnDest(){return this.dest;}
    public int returnWeight(){return this.weight;}
}
public class Main{

    //static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    //static ArrayList<Integer>[] arrayLists;
    //static boolean[] visited;
    //static int[] orders;
    //static int dfs(int v){return 0;}
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int V = Integer.parseInt(br.readLine());
        int E = Integer.parseInt(br.readLine());

        //시작점에서 최단 거리 저장
        int[] path = new int[V+1];
        for(int i = 0; i <= V; ++i){ //초기 최단 거리는 문제의 최댓값보다 크게 설정
            path[i] = 2100000000;
        }

        //인접 리스트 - list[start] = (end, weight)
        ArrayList<Pair>[] arrayLists = new ArrayList[V+1];
        for(int i = 1; i <= V; ++i){
            arrayLists[i] = new ArrayList<>();
        }

        for(int i = 0; i < E; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            arrayLists[u].add(new Pair(v, w));
        }

        //가중치를 기준으로 오름차순 정렬되는 우선순위 큐
        PriorityQueue<Pair> pq = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                return o1.returnWeight() - o2.returnWeight();
            }
        });

        //방문한 정점 확인
        boolean[] visited = new boolean[V+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        pq.add(new Pair(start, 0)); //시작 지점을 최소 힙에 넣음
        path[start] = 0; //시작점의 최단 거리는 0

        int[] parent = new int[V+1];

        while(!pq.isEmpty()){
            int node = pq.peek().returnDest();
            int weight = pq.poll().returnWeight();

            if(weight > path[node]){
                continue;
            }

            if(!visited[node]){ //아직 방문하지 않은 정점이라면
                visited[node] = true; //방문하고

                for(Pair pair : arrayLists[node]){ //node에서 갈 수 있는 간선 순회
                    //만약 node에서 갈 수 있는 거리 중 현재 기록 거리보다 더 짧은 간선이 있다면
                    if(path[pair.returnDest()] > path[node] + pair.returnWeight()){
                        path[pair.returnDest()] = path[node] + pair.returnWeight(); //거리 갱신
                        pq.add(new Pair(pair.returnDest(), path[pair.returnDest()])); //큐 삽입
                        parent[pair.returnDest()] = node;
                    }
                }
            }
        }

        for(int i = 1; i <= V; ++i){
            arrayLists[i].clear();
        }

        bw.write(path[end] + "\n");
        int cnt = 1;
        Stack<Integer> stack = new Stack<>();
        stack.push(end);
        while(end != start){
            end = parent[end];
            stack.push(end);
            cnt += 1;
        }
        bw.write(cnt + "\n");
        while(!stack.isEmpty()){
            bw.write(Integer.toString(stack.pop()));
            bw.write(" ");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}