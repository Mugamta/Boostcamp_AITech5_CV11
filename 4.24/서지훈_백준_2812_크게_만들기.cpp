#include <stack>
#include <iostream>

int main(){
	int N, K;
	std::string str;
	
	std::cin >> N >> K;
	std::cin >> str;
	
	int k = K;
	
	std::stack<char> st;
	
	for(int i = 0; i < str.length(); ++i){
		if(st.empty()){
			st.push(str.at(i));
		}
		else if(K > 0 && st.top() >= str.at(i)){
			st.push(str.at(i));
		}
		else{
			while(!st.empty() && K > 0 && st.top() < str.at(i)){
				st.pop();
				K -= 1;
			}
			st.push(str.at(i));
		}
	}
	
	std::stack<char> st2;
	while(!st.empty()){
		st2.push(st.top());
		st.pop();
	}
	int cnt = 0;
	while(cnt++ < N - k){
		std::cout << st2.top();
		st2.pop();
	}
	
}