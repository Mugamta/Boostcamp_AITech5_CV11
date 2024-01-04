import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class UnionFind{
    private int[] parent;
    private final int parent_length;
    public UnionFind(int N){
        this.parent_length = N+2;
        this.init();
    }
    public void init(){
        parent = new int[parent_length];
        for(int i = 1; i < parent_length; ++i){
            parent[i] = i;
        }
    }
    public void union(int a, int b){
        int rootA = this.find(a);
        int rootB = this.find(b);
        if(rootA >= rootB){
            parent[rootA] = rootB;
        }
        else{
            parent[rootB] = rootA;
        }
    }
    public int find(int target){
        if(target == this.parent[target]) return target;
        int parent_idx = find(parent[target]);
        return parent[target] = parent_idx;
    }
}

class Tuple{
    private final int start, end, width;
    public Tuple(int a, int b, int c){
        this.start = a;
        this.end = b;
        this.width = c;
    }
    public int returnStart(){return this.start;}
    public int returnEnd(){return this.end;}
    public int returnWidth(){return this.width;}
}

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        PriorityQueue<Tuple> pq = new PriorityQueue<>((o1, o2) -> o2.returnWidth() - o1.returnWidth());

        for(int i = 0; i < w; ++i){
            st = new StringTokenizer(br.readLine());
            int w_start = Integer.parseInt(st.nextToken());
            int w_end = Integer.parseInt(st.nextToken());
            int w_width = Integer.parseInt(st.nextToken());
            pq.add(new Tuple(w_start, w_end, w_width));
        }

        UnionFind uf = new UnionFind(p);

        while(!pq.isEmpty()){
            int w_start = pq.peek().returnStart();
            int w_end = pq.peek().returnEnd();
            int w_width = pq.poll().returnWidth();

            uf.union(w_start, w_end);

            if(uf.find(c) == uf.find(v)){
                bw.write(Integer.toString(w_width));
                break;
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}