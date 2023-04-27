#include <iostream>
#include <queue>
#include <tuple>

bool visited[2][1001][1001];

int main(){
	int N, M, Hx, Hy, Ex, Ey;
	std::cin >> N >> M;
	std::cin >> Hy >> Hx;
	std::cin >> Ey >> Ex;
	
	Hx -= 1;
	Hy -= 1;
	Ex -= 1;
	Ey -= 1;
	
	int matrix[1001][1001];
	for(int i = 0; i < N; ++i){
		for(int j = 0; j < M; ++j){
			std::cin >> matrix[i][j];
		}
	}
	
	visited[0][Hy][Hx] = true;
	
	std::queue< std::tuple<int, int, int, int> > q;
	q.push(std::make_tuple(Hx, Hy, 0, 0));
	
	int plus_x[4] = {1, -1, 0, 0};
	int plus_y[4] = {0, 0, 1, -1};
	
	int result = N * M + 1;
	
	while(!q.empty()){
		int x = std::get<0>(q.front());
		int y = std::get<1>(q.front());
		int time = std::get<2>(q.front());
		int flag = std::get<3>(q.front());
		q.pop();
		
		if(x == Ex && y == Ey){
			if(result > time){
				result = time;
			}
            continue;
        }

		
		for(int i = 0; i < 4; ++i){
            int next_x = x + plus_x[i];
            int next_y = y + plus_y[i];

            if(0 <= next_x && next_x < M && 0 <= next_y && next_y < N) {
                if(flag == 1){
                    if(!visited[1][next_y][next_x] &&  matrix[next_y][next_x] ==0){
                        q.push(std::make_tuple(next_x, next_y, time + 1, 1));
                        visited[1][next_y][next_x] = true;
                    }
                }

                else {
                    if(!visited[0][next_y][next_x]){
                        if(matrix[next_y][next_x] == 1){
                            q.push(std::make_tuple(next_x, next_y, time + 1, 1));
                            visited[1][next_y][next_x] = true;
                        }

                        else{
                            q.push(std::make_tuple(next_x, next_y, time + 1, 0));
                            visited[0][next_y][next_x] = true;
                        }

                    }
                }
            }
        }
	}
	
	if(result == N * M + 1){
		std::cout << "-1";
	}
	else{
		std::cout << result;
	}
}