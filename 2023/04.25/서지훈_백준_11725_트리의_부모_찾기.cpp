#include <iostream>
#include <vector>

int parent[100001];
std::vector<int> adjacent[100001];
bool visited[100001];

void dfs(int node){
	for(auto next_node : adjacent[node]){
		if(!visited[next_node]){
			visited[next_node] = true;
			parent[next_node] = node;
			dfs(next_node);
		}
	}
}

int main(){
	int N;
	std::cin >> N;
	
	for(int i = 0; i < N-1; ++i){
		int a, b;
		std::cin >> a >> b;
		adjacent[a].push_back(b);
		adjacent[b].push_back(a);
	}
	
	visited[1] = true;
	
	dfs(1);
	
	for(int i = 2; i <= N; ++i){
		std::cout << parent[i] << '\n';
	}
}