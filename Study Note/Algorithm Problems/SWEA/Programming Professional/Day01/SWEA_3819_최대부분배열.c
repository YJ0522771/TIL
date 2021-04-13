#include <stdio.h>
int A[200000];
int main(void)
{
    int test_case;
    int T, N, i, temp, res;

    scanf("%d", &T);
    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%d", &N);
        for (i = 0; i < N; i++)
            scanf("%d", &A[i]);
        temp = 0;
        res = -1001;
        for (i = 0; i < N; i++)
        {
            temp += A[i];
            if (res < temp)
                res = temp;
            if (temp < 0)
                temp = 0;
        }
        printf("#%d %d\n",  test_case, res);
    }
    return 0; 
}