import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int k = K;

        String num = br.readLine();

        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < num.length(); ++i){
            if(stack.isEmpty()){
                stack.push(num.charAt(i) - '0');
            }
            else if(!stack.isEmpty() && stack.peek() >= num.charAt(i) - '0'){
                stack.push(num.charAt(i) - '0');
            }
            else{
                while(!stack.isEmpty() && K > 0 && stack.peek() < num.charAt(i) - '0'){
                    stack.pop();
                    K -= 1;
                }
                stack.push(num.charAt(i) - '0');
            }
        }

        int cnt = 0;
        for(Integer ele : stack){
            if(cnt++ < N - k){
                bw.write(Integer.toString(ele));
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
