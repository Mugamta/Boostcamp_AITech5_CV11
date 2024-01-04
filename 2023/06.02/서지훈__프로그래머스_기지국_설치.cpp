#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer = 0;

    double radio = 2 * w + 1;
    answer += int(ceil((stations[0] - w - 1) / radio));

    for(int i = 0; i < stations.size()-1; ++i){
        answer += int(ceil((stations[i+1] - stations[i] - 2 * w - 1) / radio));
    }
        
    answer += int(ceil((n - stations[stations.size()-1] - w) / radio));

    return answer;
}