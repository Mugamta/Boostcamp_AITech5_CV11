/*
 * 23:15 [START]
 *       1) 1 <= works <= 2 * 1e4, 1 <= n <= 1e6 -> O(n * log(n))
 * 23:19 2) Greedy: Decrease max(works[i]) by 1. -> log(n) -> max_pq<>
 * 23:27 [AC]
 */

#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;

    priority_queue<long long int> max_pq;
    
    for (auto& work : works) {
        max_pq.emplace(work);
    }
    
    for (long long int tmp; n-- && !max_pq.empty(); ) {
        tmp = max_pq.top();
        
        max_pq.pop();
        
        if (1 < tmp) {
            max_pq.emplace(tmp - 1);
        }
    }
    
    for (; !max_pq.empty(); max_pq.pop()) {
        answer += max_pq.top() * max_pq.top();
    }
    
    return answer;
}