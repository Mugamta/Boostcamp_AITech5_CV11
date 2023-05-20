#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>

class UnionFind{
	private:
		int parent[1001];
		void init(int N) {
			for(int i = 0; i <= 1000; ++i){
				parent[i] = i;
			}
		}
	public:
		UnionFind(int N) {
			init(N);
		}
		int find(int target){
			if(target == parent[target]) return target;
			parent[target] = find(parent[target]);
            return parent[target];
		}
		void union_element(int a, int b){
			a = find(a);
			b = find(b);
			if(a >= b){
				parent[a] = b;
			}
			else{
				parent[b] = a;
			}
		}
		bool is_union(int a, int b){
			if(find(a) == find(b)) return true;
			return false;
		}
};

typedef std::tuple<int,int,int> t;

class Compare {
    public:
       bool operator()(t a, t b){
           if(std::get<2>(a) > std::get<2>(b)){
               return true;
           }
           return false;
      }
};

int main(){
	int N, M;
	std::cin >> N >> M;
	
	char MW[1001];
	for(int i = 1; i <= N; ++i){
		std::cin >> MW[i];
	}

	UnionFind uf(N);
	std::priority_queue<t, std::vector<t>, Compare > pq;
	
	for(int i = 0; i < M; ++i){
		int start, end, length;
		std::cin >> start >> end >> length;
		pq.push(std::make_tuple(start, end, length));
	}
	
	int result = 0;
	int check = 1;
	
	while(!pq.empty()){
		int start = std::get<0>(pq.top());
		int end = std::get<1>(pq.top());
		int length = std::get<2>(pq.top());
		pq.pop();
		
		if(MW[start] != MW[end] and !uf.is_union(start, end)){
			uf.union_element(start, end);
			result += length;
			check += 1;
		}
	}
	
	if(check < N) std::cout << -1;
	else std::cout << result;
}