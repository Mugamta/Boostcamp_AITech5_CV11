import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Tuple{
    private final int first;
    private final int second;
    Tuple(int first, int second){
        this.first = first;
        this.second = second;
    }
    public int returnFirst(){
        return this.first;
    }
    public int returnSecond(){
        return this.second;
    }
}

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        ArrayList<Tuple> arrayList = new ArrayList<>();

        for(int i = 0; i < N; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int P = Integer.parseInt(st.nextToken());
            int Q = Integer.parseInt(st.nextToken());
            arrayList.add(new Tuple(P, Q));
        }

        arrayList.sort(Comparator.comparingInt(Tuple::returnFirst));

        int max_idx = 1;

        PriorityQueue<Tuple> pq = new PriorityQueue<>((t1, t2) -> {
            if(t1.returnFirst() == t2.returnFirst()) return t1.returnSecond() - t2.returnSecond();
            return t1.returnFirst() - t2.returnFirst();
        });

        PriorityQueue<Integer> idx_pq = new PriorityQueue<>();
        for(int i = 1; i <= N; ++i){
            idx_pq.add(i);
        }

        int[] counts = new int[N+1];

        for(int i = 0; i < N; ++i){
            int start_time = arrayList.get(i).returnFirst();
            int end_time = arrayList.get(i).returnSecond();

            //System.out.printf("현재 시작 시간은 %d, 종료 시간은 %d\n", start_time, end_time);
            //System.out.println("현재 사지방 이용 인원은 " + pq.size());
            //if(!pq.isEmpty()) System.out.printf("가장 먼저 종료되는 사지방 이용자의 시간은 %d\n", pq.peek().returnFirst());

            if(!pq.isEmpty() && pq.peek().returnFirst() <= start_time){

                while(!pq.isEmpty() && pq.peek().returnFirst() <= start_time){
                    idx_pq.add(pq.poll().returnSecond());
                }

                //System.out.println("-먼저 종료된 사지방 이용자의 자리 " + idx_pq.peek() + " 이용");
                //System.out.println("남은 사지방 이용 인원은 " + pq.size() + "\n");
                counts[idx_pq.peek()] += 1;
                pq.add(new Tuple(end_time, idx_pq.poll()));
            }else{
                //System.out.println("-종료된 사지방 이용자가 없으므로 새 자리 " + idx_pq.peek() + " 이용\n");
                counts[idx_pq.peek()] += 1;
                pq.add(new Tuple(end_time, idx_pq.peek()));
                idx_pq.poll();
            }

            if(idx_pq.isEmpty()) max_idx = N;
            else max_idx = Math.max(max_idx, idx_pq.peek()-1);
        }

        bw.write(Integer.toString(max_idx));
        bw.write("\n");
        for(int i = 1; i <= max_idx; ++i){
            bw.write(Integer.toString(counts[i]));
            bw.write(" ");
        }


        bw.flush();
        br.close();
        bw.close();
    }
}