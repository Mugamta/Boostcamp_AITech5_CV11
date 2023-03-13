#include <iostream>
#include <utility>

long long dp[1500][1500];

int main()
{
	int N;
    std::cin >> N;
    
    std::pair<int, int> arr[1500];
    
    for(int i = 0; i < N; ++i){
    	int x, y;
    	std::cin >> x >> y;
    	arr[i] = std::make_pair(x, y);
	}
	
	int result = 0;
	
	for(int i = 0; i < N; ++i){
        long long x1 = arr[i].first;
        long long y1 = arr[i].second;
        for(int j = i+1; j < N; ++j){
            long long x2 = arr[j].first;
        	long long y2 = arr[j].second;
            for(int k = j+1; k < N; ++k){
                long long x3 = arr[k].first;
        		long long y3 = arr[k].second;

                if(dp[i][j] == 0) dp[i][j] = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                if(dp[i][k] == 0) dp[i][k] = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3);
                if(dp[j][k] == 0) dp[j][k] = (x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3);
                
                if (dp[i][j] == dp[i][k] + dp[j][k] || dp[i][k] == dp[i][j] + dp[j][k] || dp[j][k] == dp[i][j] + dp[i][k]) {
                    result += 1;
                }
            }
        }
    }
    std::cout << result;
}
