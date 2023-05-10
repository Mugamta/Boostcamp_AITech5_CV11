import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        
        Deque<Integer> dq1 = Arrays.stream(queue1).boxed().collect(Collectors.toCollection(ArrayDeque::new));
        Deque<Integer> dq2 = Arrays.stream(queue2).boxed().collect(Collectors.toCollection(ArrayDeque::new));
        
        long sum1 = 0;
        long sum2 = 0;
        long max = (dq1.size() + dq2.size()) * 2;

        for(Integer ele : dq1)
            sum1 += ele;
        for(Integer ele : dq2)
            sum2 += ele;
    
        while(sum1 != sum2 && answer <= max){
            if(sum1 > sum2){
                sum1 -= dq1.peek();
                sum2 += dq1.peek();
                dq2.add(dq1.pollFirst());
            }
            else{
                sum1 += dq2.peek();
                sum2 -= dq2.peek();
                dq1.add(dq2.pollFirst());
            }
            answer += 1;
        }
    
        if(answer > max){
            answer = -1;
        }
        
        return answer;
    }
}