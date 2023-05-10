#include <iostream>
#include <tuple>
#include <queue>
#include <vector>
#include <algorithm>

class UnionFind{
	private:
		int parent[1000];
		void init(int N) {
			for(int i = 0; i < 1000; ++i){
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
           if(std::get<2>(a) < std::get<2>(b)){
               return true;
           }
           return false;
      }
};

int main(){
	int p, w, c, v;
	std::cin >> p >> w >> c >> v;
	
	UnionFind uf(p);
	std::priority_queue<t, std::vector<t>, Compare > pq;
	
	for(int i = 0; i < w; ++i){
		int w_start, w_end, w_width;
		std::cin >> w_start >> w_end >> w_width;
		pq.push(std::make_tuple(w_start, w_end, w_width));
	}
	
	while(!pq.empty()){
		int w_start = std::get<0>(pq.top());
		int w_end = std::get<1>(pq.top());
		int w_width = std::get<2>(pq.top());
		pq.pop();
		
		uf.union_element(w_start, w_end);
		
		if(uf.is_union(c, v)){
			std::cout << w_width;
			break;
		}
	}
}