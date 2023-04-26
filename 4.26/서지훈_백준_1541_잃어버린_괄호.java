import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String expr = br.readLine();

        int result = 0, start = 0, end = 0, idx = 0;

        while(idx <= expr.length()){
            if(idx == expr.length() || expr.charAt(idx) == '+'){
                result += Integer.parseInt(expr.substring(start, end));
                idx += 1;
                start = idx;
                end = idx;
                continue;
            }
            else if(expr.charAt(idx) == '-'){
                result += Integer.parseInt(expr.substring(start, end));
                idx += 1;
                start = idx;
                end = idx;
                break;
            }
            end += 1;
            idx += 1;
        }

        while(idx <= expr.length()){
            if(idx == expr.length() || expr.charAt(idx) == '+' || expr.charAt(idx) == '-'){
                result -= Integer.parseInt(expr.substring(start, end));
                idx += 1;
                start = idx;
                end = idx;
                continue;
            }
            end += 1;
            idx += 1;
        }

        bw.write(Integer.toString(result));

        bw.flush();
        bw.close();
        br.close();
    }
}
