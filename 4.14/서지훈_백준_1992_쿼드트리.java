import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[][] video;
    static BufferedWriter bw;
    public static void recursion(int N, int x, int y) throws IOException {
        int check = video[y][x];

        for(int i = y; i < y + N; ++i){
            for(int j = x; j < x + N; ++j){
                if(check != video[i][j]){
                    bw.write("(");

                    recursion(N / 2, x, y);
                    recursion(N / 2, x + N / 2, y);
                    recursion(N / 2, x, y + N / 2);
                    recursion(N / 2, x + N / 2, y + N / 2);

                    bw.write(")");

                    return;
                }
            }
        }

        if (check == 0) bw.write("0");
        else bw.write("1");
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        video = new int[N][N];

        for(int i = 0; i < N; ++i){
            String str = br.readLine();
            for(int j = 0; j < N; ++j){
                video[i][j] = str.charAt(j) - '0';
            }
        }

        recursion(N, 0, 0);

        bw.flush();
        bw.close();
        br.close();
    }
}
