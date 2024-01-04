#include <iostream>
#include <vector>

std::vector<int> adjacent[100000];
bool visited[100000];
int apples[100000];
int result = 0;

int n, k;

void dfs(int node, int distance){
	if(k > distance){
		for(auto next_node : adjacent[node]){
			if(!visited[next_node]){
				visited[next_node] = true;
				result += apples[next_node];
				dfs(next_node, distance+1);
			}
		}
	}
}

int main(){
	std::cin >> n >> k;
	
	for(int i = 0; i < n-1; ++i){
		int p, c;
		std::cin >> p >> c;
		adjacent[p].push_back(c);
		adjacent[c].push_back(p);
	}
	
	for(int i = 0; i < n; ++i){
		std::cin >> apples[i];
	}
	
	visited[0] = true;
	result = apples[0];
	
	dfs(0, 0);
	
	std::cout << result;
}