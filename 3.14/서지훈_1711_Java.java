import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Pair{
    private final long x, y;
    public Pair(long x, long y){
        this.x = x;
        this.y = y;
    }
    public long returnX(){return this.x;}
    public long returnY(){return this.y;}
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        long [][] dp = new long[N][N];
        ArrayList<Pair> arrayList = new ArrayList<>();
        StringTokenizer st;
        for(int i = 0; i < N; ++i){
            st = new StringTokenizer(br.readLine());
            arrayList.add(new Pair(Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())));
        }

        int result = 0;

        for(int i = 0; i < N; ++i){
            long x1 = arrayList.get(i).returnX();
            long y1 = arrayList.get(i).returnY();
            for(int j = i+1; j < N; ++j){
                long x2 = arrayList.get(j).returnX();
                long y2 = arrayList.get(j).returnY();
                for(int k = j+1; k < N; ++k){
                    long x3 = arrayList.get(k).returnX();
                    long y3 = arrayList.get(k).returnY();

                    if(dp[i][j] == 0) dp[i][j] = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                    if(dp[i][k] == 0) dp[i][k] = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3);
                    if(dp[j][k] == 0) dp[j][k] = (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3);

                    if (dp[i][j] == dp[i][k] + dp[j][k] || dp[i][k] == dp[i][j] + dp[j][k] || dp[j][k] == dp[i][j] + dp[i][k]) {
                        result += 1;
                    }
                }
            }
        }

        System.out.println(result);

        bw.flush();
        bw.close();
        br.close();
    }
}
