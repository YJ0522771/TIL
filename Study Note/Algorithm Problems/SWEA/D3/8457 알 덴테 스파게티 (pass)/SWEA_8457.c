#include <stdio.h>
int main(void)
{
    int test_case;
    int T, N, B, E, temp, res, i, j;

    scanf("%d", &T);
    
    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%d %d %d", &N, &B, &E);
        temp = B - E;
        B += E;
        E = temp;
        res = 0;
        for (i = 0; i < N; i++)
        {
          scanf("%d", &temp);
          for (j = E; j <= B; j++)
              if (j % temp == 0)
              {
                  res++;
                  break;
              }
        }
        printf("#%d %d\n", test_case, res);
    }
    return 0;
}