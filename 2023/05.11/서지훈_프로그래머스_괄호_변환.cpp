#include <string>
#include <stack>
#include <iostream>

using namespace std;

bool check(string u){
    stack<int> st;
    int length = 0;
    for(auto ele : u){
        if (ele == '('){
            st.push(ele);
            length += 1;
        }
        else{
            if (length == 0){
                return false;
            }
            else if(st.top() == '('){
                st.pop();
                length -= 1;
            }
        }
    }
    return true;
}

string solution(string p) {
    if(p.length() == 0){
        return p;
    }
    
    int left = 0;
    int right = 0;
    int idx = 0;
    while(idx < p.length() && (left != right || left + right == 0)){
        if(p.at(idx) == '(')
            left += 1;
        else if(p.at(idx) == ')')
            right += 1;
        idx += 1;
    }

    string u = p.substr(0, idx);
    string v = "";
    if(idx + 1 < p.length()){
    	v = p.substr(idx);
	}
    
    //std::cout << u << " " << v << "\n";
    
    if(left != right){
        u = "";
        string v(p);
    }
        
    if(check(u) == true)
        return u + solution(v);
    else{
        string s = "";
        for(auto i : u.substr(1, u.length()-2)){
            if(i == '(') s += ')';
            else s += '(';
    	}
    	return '(' + solution(v) + ')' + s;
    }
}

int main(){
	cout << solution("(()())()") << '\n';
	cout << "(()())()\n\n";
	
	cout << solution(")(") << '\n';
	cout << "()\n\n";
	
	cout << solution("()))((()") << '\n';
	cout << "()(())()\n\n";
}