#include <iostream>

int min(int a, int b){
	if(a > b) return b;
	return a;
}
int min(int a, int b, int c){
	if(a >= c && b >= c) return c;
	if(a >= b && c >= b) return b;
	if(b >= a && c >= a) return a;
}

int main(){
	int N;
	std::cin >> N;
	
	int dp[N][3];
	std::cin >> dp[0][0] >> dp[0][1] >> dp[0][2];
	
	for(int i = 1; i < N; ++i){
		int R, G, B;
		std::cin >> R >> G >> B;
		
		dp[i][0] = R + min(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = G + min(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] = B + min(dp[i - 1][0], dp[i - 1][1]);
	}
	
	std::cout << min(dp[N-1][0], dp[N-1][1], dp[N-1][2]);
}