import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

class Pair{
    private final int x, y, time, flag;
    public Pair(int x, int y, int time, int flag){
        this.x = x;
        this.y = y;
        this.time = time;
        this.flag = flag;
    }
    public int returnX(){return this.x;}
    public int returnY(){return this.y;}
    public int returnTime(){return this.time;}
    public int returnFlag(){return this.flag;}
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int Hy = Integer.parseInt(st.nextToken()) - 1;
        int Hx = Integer.parseInt(st.nextToken()) - 1;

        st = new StringTokenizer(br.readLine());
        int Ey = Integer.parseInt(st.nextToken()) - 1;
        int Ex = Integer.parseInt(st.nextToken()) - 1;

        int[][] matrix = new int[N][M];
        for(int i = 0; i < N; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; ++j){
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean [][][] visited = new boolean[2][N][M];

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(Hx, Hy, 0, 0));

        int[] plus_x = {1, -1, 0, 0};
        int[] plus_y = {0, 0, 1, -1};

        int result = N * M + 1;
        while(!q.isEmpty()){
            int x = q.peek().returnX();
            int y = q.peek().returnY();
            int time = q.peek().returnTime();
            int flag = q.poll().returnFlag();

            if(x == Ex && y == Ey){
                result = Math.min(result, time);
                continue;
            }

            for(int i = 0; i < 4; ++i){
                int next_x = x + plus_x[i];
                int next_y = y + plus_y[i];

                if(0 <= next_x && next_x < M && 0 <= next_y && next_y < N) {
                    if(flag == 1){
                        if(!visited[ 1][next_y][next_x] &&  matrix[next_y][next_x] ==0){
                            q.add(new Pair(next_x, next_y, time + 1, 1));
                            visited[1][next_y][next_x] = true;
                        }
                    }

                    else {
                        if(!visited[0][next_y][next_x]){
                            if(matrix[next_y][next_x] == 1){
                                q.add(new Pair(next_x, next_y, time + 1, 1));
                                visited[1][next_y][next_x] = true;
                            }

                            else{
                                q.add(new Pair(next_x, next_y, time + 1, 0));
                                visited[0][next_y][next_x] = true;
                            }

                        }
                    }
                }
            }
        }

        if(result == N * M + 1){
            System.out.println("-1");
        }
        else{
            System.out.println(Integer.toString(result));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
