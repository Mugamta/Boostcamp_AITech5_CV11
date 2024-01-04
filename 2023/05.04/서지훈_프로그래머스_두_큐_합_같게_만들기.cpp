#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0;
    
    deque<int> dq1(queue1.begin(), queue1.end());
    deque<int> dq2(queue2.begin(), queue2.end());
    
    long long sum1 = 0;
    long long sum2 = 0;
    long long max = (dq1.size() + dq2.size()) * 2;
    
    for(auto ele : dq1)
        sum1 += ele;
    for(auto ele : dq2)
        sum2 += ele;
    
    while(sum1 != sum2 && answer <= max){
        if(sum1 > sum2){
            sum1 -= dq1.front();
            sum2 += dq1.front();
            dq2.push_back(dq1.front());
            dq1.pop_front();
        }
        else{
            sum1 += dq2.front();
            sum2 -= dq2.front();
            dq1.push_back(dq2.front());
            dq2.pop_front();
        }
        answer += 1;
    }
    
    if(answer > max)
        answer = -1;
    
    return answer;
}