#include <iostream>
#include <string>

int video[64][64];

void recursion(int N, int x, int y){
    int check = video[y][x];

    for(int i = y; i < y + N; ++i){
        for(int j = x; j < x + N; ++j){
            if(check != video[i][j]){
                std::cout << "(";

                recursion(N / 2, x, y);
                recursion(N / 2, x + N / 2, y);
                recursion(N / 2, x, y + N / 2);
                recursion(N / 2, x + N / 2, y + N / 2);

                std::cout << ")";

                return;
            }
        }
    }

    if (check == 0) std::cout << "0";
    else std::cout << "1";
}

int main(){
	int N;
	std::cin >> N;
	
	std::string str;
	
	for(int i = 0; i < N; ++i){
		std::cin >> str;
		for(int j = 0; j < N; ++j){
			video[i][j] = str.at(j) - '0';
		}
	}
	
	recursion(N, 0, 0);
}
