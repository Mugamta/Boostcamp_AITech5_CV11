#include <cstdio>

using namespace std;

int answer;

int main() {
    for (int val, is_valid = 1; -1 != scanf("%d", &val); ) {
        if (is_valid && 0 < val) {
            answer += val;
        }
        else {
            is_valid = 0;
            answer -= (0 < val) ? val : -val;
        }
    }

    printf("%d", answer);

    return 0;
}