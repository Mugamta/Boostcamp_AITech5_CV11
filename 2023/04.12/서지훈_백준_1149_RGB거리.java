import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N+1][3];

        for(int i = 1; i <= N; ++i){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            int G = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            dp[i][0] = R + Math.min(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = G + Math.min(dp[i - 1][0], dp[i - 1][2]);
            dp[i][2] = B + Math.min(dp[i - 1][0], dp[i - 1][1]);
        }

        bw.write(Integer.toString(Math.min(dp[N][0], Math.min(dp[N][1], dp[N][2]))));

        bw.flush();
        bw.close();
        br.close();
    }
}
