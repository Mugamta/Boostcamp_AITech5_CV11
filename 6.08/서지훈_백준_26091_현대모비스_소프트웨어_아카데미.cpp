#include <iostream>
#include <algorithm>

int main(){
	int N, M;
	std::cin >> N >> M;
	int *arr = new int[N];
	for(int i = 0; i < N; ++i){
		std::cin >> arr[i];
	}
	
	std::sort(arr, arr+N);
	
	int left = 0, right = N-1;
	
	int result = 0;
	while(left < right){
		if(arr[left] + arr[right] >= M){
			result += 1;
			right -= 1;
		}
		left += 1;
	}
	std::cout << result;
	
	delete arr;
}