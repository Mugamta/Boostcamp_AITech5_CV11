class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;

        double radio = 2 * w + 1;
        answer += (int)(Math.ceil((stations[0] - w - 1) / radio));

        for(int i = 0; i < stations.length-1; ++i){
            answer += (int)(Math.ceil((stations[i+1] - stations[i] - 2 * w - 1) / radio));
        }

        answer += (int)(Math.ceil((n - stations[stations.length-1] - w) / radio));

        return answer;
    }
}