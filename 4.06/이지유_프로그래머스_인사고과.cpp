/*
 * 10:50 [START]
 * 10:54 [FORMULATION] Brute-forcing
 * 11:01 [REFORMULATION]
 * 11:04 [FORMULATION] Sorting
 * 11:24 [WA, 36%] fix remove non-incentives logic
 * 11:34 [WA, 52%] fix remove non-incentives logic (tmp_b assignment)
 * 11:39 [WA, 44%] fix remove non-incentives logic (tmp_b assignment)
 * 11:48 [WA, 60%] fix find rank logic (cnt reassignment)
 * 11:52 [AC]
 */

#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int solution(vector<vector<int>> scores) {
    int answer = 1;
    
    // Save target scores.
    int a = scores[0][0], b = scores[0][1], sum = scores[0][0] + scores[0][1];
    
    // Remove non-incentivized employees.
    sort(scores.begin(), scores.end(), greater());
    
    int i = 0, endi = scores.size(), max_b = scores[0][1];
    vector<int> sums;
    
    for (; endi > i && scores[0][0] == scores[i][0]; ++i) {
        sums.emplace_back(scores[i][0] + scores[i][1]);
    }
    for (; endi > i && -1 != answer; ) {
        int tmp_a = scores[i][0];
        int tmp_b = scores[i][1];
        
        for (; endi > i && tmp_a == scores[i][0] && -1 != answer; ++i) {
            if (max_b <= scores[i][1]) {
                sums.emplace_back(scores[i][0] + scores[i][1]);
            }
            else {
                if (scores[i][0] == a && scores[i][1] == b) {
                    answer = -1;
                }
            }
        }
        
        if (tmp_b > max_b) {
            max_b = tmp_b;
        }
    }
    
    // Find rank.
    if (-1 != answer) {
        sort(sums.begin(), sums.end());
        
        answer = sums.end() - upper_bound(sums.begin(), sums.end(), sum) + 1;
    }
    
    return answer;
}