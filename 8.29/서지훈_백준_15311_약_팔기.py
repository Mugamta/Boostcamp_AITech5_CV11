"""
최대 약 요구량이 주어지므로, 1 ~ N개의 약을 모두 표현할 수 있어야 한다.
약 판매대는 봉지가 최대 2000개까지만 지원된다.
N은 최대 100만이므로, 최대 500개의 봉지가 필요하다.

즉, 1500개의 남은 봉지로 모든 수를 표현해야 한다.
500개의 봉지에 2000개를 담을 수 있으므로, 1000개의 봉지에 1000개를 담을 수 있다.
즉, 나머지 1000개의 봉지를 이용하여 남은 수를 표현하면 된다.
이 문제는 연속된 알약 봉지를 집어야 하므로, 1000개의 봉지에 모두 1을 담아보자.

이렇게 되면 1000개의 1이 든 봉지와,
1000개의 1000이 든 봉지가 생긴다.


"""
import sys

input()
sys.stdout.write('2000\n')
for i in range(1000):
    sys.stdout.write('1000 ')
for i in range(1000):
    sys.stdout.write('1 ')

