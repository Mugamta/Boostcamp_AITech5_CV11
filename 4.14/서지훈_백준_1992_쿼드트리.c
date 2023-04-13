#include <stdio.h>

int video[64][64];

void recursion(int N, int x, int y){
    int check = video[y][x];

	int i, j;
    for(i = y; i < y + N; ++i){
        for(j = x; j < x + N; ++j){
            if(check != video[i][j]){
                printf("(");

                recursion(N / 2, x, y);
                recursion(N / 2, x + N / 2, y);
                recursion(N / 2, x, y + N / 2);
                recursion(N / 2, x + N / 2, y + N / 2);

                printf(")");

                return;
            }
        }
    }

    if (check == 0) printf("0");
    else printf("1");
}

int main(){
	int N;
	scanf("%d", &N);
	
	char str[65];
	
	int i, j;
	for(i = 0; i < N; ++i){
		scanf("%s", &str);
		for(j = 0; j < N; ++j){
			video[i][j] = str[j] - '0';
		}
	}
	
	recursion(N, 0, 0);
}
