#include <stdio.h>
#include <math.h>
int main(void)
{
    int test_case;
    int T;
    int N;
    int x, y;
    int i;
    double temp;
    int result;

    freopen("input.txt", "r", stdin);
    setbuf(stdout, NULL);
    scanf("%d", &T);

    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%d", &N);
        result = 0;
        for(i = 0; i < N; i++)
        {
            scanf("%d %d", &x, &y);
            temp = (x * x) + (y * y);
            temp = sqrt(temp);
            if(temp == 0)
            {
                result += 10;
            }
            else if(temp <= 200)
            {
                result += (11 - ceil(temp / 20));
            }
        }
        printf("#%d %d\n", test_case, result);
    }
    return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
