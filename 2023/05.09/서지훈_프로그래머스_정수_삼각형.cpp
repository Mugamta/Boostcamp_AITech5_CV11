#include <string>
#include <vector>

using namespace std;

int max(int a, int b){
    if(a > b) return a;
    return b;
}

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    
    int length = triangle.size();
    
    for(int i = 1; i < length; ++i){
        triangle[i][0] += triangle[i-1][0];
        
        for(int j = 1; j < i; ++j){
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]);
        }
        triangle[i][i] += triangle[i-1][i-1];
    }
    
    for(auto ele : triangle[length-1]){
        answer = max(answer, ele);
    }
    
    return answer;
}