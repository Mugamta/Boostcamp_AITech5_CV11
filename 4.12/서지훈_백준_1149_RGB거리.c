#include <stdio.h>

int min2(int a, int b){
	if(a > b) return b;
	return a;
}
int min3(int a, int b, int c){
	if(a >= c && b >= c) return c;
	if(a >= b && c >= b) return b;
	if(b >= a && c >= a) return a;
}

int main(){
	int N;
	scanf("%d", &N);
	
	int dp[N][3];
	scanf("%d %d %d", &dp[0][0], &dp[0][1], &dp[0][2]);
	
	for(int i = 1; i < N; ++i){
		int R, G, B;
		scanf("%d %d %d", &R, &G, &B);
		
		dp[i][0] = R + min2(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = G + min2(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] = B + min2(dp[i - 1][0], dp[i - 1][1]);
	}
	
	printf("%d", min3(dp[N-1][0], dp[N-1][1], dp[N-1][2]));
}