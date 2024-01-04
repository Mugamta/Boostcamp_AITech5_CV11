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
        this.parent = new int[parent_length];
        for(int i = 1; i < parent_length; ++i){
            this.parent[i] = i;
        }
    }
    public void union(int a, int b){
        int rootA = this.find(a);
        int rootB = this.find(b);
        if(rootA >= rootB){
            this.parent[rootA] = rootB;
        }
        else{
            this.parent[rootB] = rootA;
        }
    }
    public int find(int target){
        if(target == this.parent[target]) return target;
        int parent_idx = this.find(this.parent[target]);
        return this.parent[target] = parent_idx;
    }

    public boolean is_union(int a, int b){
        return this.find(a) == this.find(b);
    }
}

class Tuple{
    private final int start, end, length;
    public Tuple(int a, int b, int c){
        this.start = a;
        this.end = b;
        this.length = c;
    }
    public int returnStart(){return this.start;}
    public int returnEnd(){return this.end;}
    public int returnLength(){return this.length;}
}

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[] MW = new char[1001];
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; ++i){
            MW[i] = st.nextToken().charAt(0);
        }

        UnionFind uf = new UnionFind(N);
        PriorityQueue<Tuple> pq = new PriorityQueue<>(Comparator.comparingInt(Tuple::returnLength));

        for(int i = 0; i < M; ++i){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int length = Integer.parseInt(st.nextToken());
            pq.add(new Tuple(start, end, length));
        }

        int result = 0;
        int check = 1;

        while(!pq.isEmpty()){
            int start = pq.peek().returnStart();
            int end = pq.peek().returnEnd();
            int length = pq.peek().returnLength();
            pq.poll();

            if(MW[start] != MW[end] && !uf.is_union(start, end)){
                uf.union(start, end);
                result += length;
                check += 1;
            }
        }

        if(check < N) bw.write("-1");
        else bw.write(Integer.toString(result));

        bw.flush();
        br.close();
        bw.close();
    }
}