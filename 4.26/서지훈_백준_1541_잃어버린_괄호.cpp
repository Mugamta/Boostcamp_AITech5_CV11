#include <iostream>
#include <string>

int main(){
	std::string expr;
	std::cin >> expr;
	
	int result = 0, start = 0, end = 0, idx = 0;
	
	while(idx <= expr.length()){
		if(idx == expr.length() || expr[idx] == '+'){
	        result += stoi(expr.substr(start, end-start));
	        idx += 1;
	        start = idx;
	        end = idx;
	        continue;
		}
	    else if(expr[idx] == '-'){
	        result += stoi(expr.substr(start, end-start));
	        idx += 1;
	        start = idx;
	        end = idx;
	        break;
		}
		end += 1;
		idx += 1;
	}
	
	while(idx <= expr.length()){
		if(idx == expr.length() || expr[idx] == '+' || expr[idx] == '-'){
	        result -= stoi(expr.substr(start, end-start));
	        idx += 1;
	        start = idx;
	        end = idx;
	        continue;
		}
		end += 1;
		idx += 1;
	}
	
	std::cout << result;
}