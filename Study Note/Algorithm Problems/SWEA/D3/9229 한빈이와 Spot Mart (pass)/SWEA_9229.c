#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M, a_min, i, j, res, temp;
	
	scanf("%d", &T);
    
	for (test_case = 1; test_case <= T; ++test_case)
	{
    scanf("%d %d", &N, &M);
    int a[N];
    a_min = 1000000;
    for (i = 0; i < N; i++)
    {
      scanf("%d", &a[i]);
      if (a[i] < a_min)
        a_min = a[i];
    }
    res = 0;
    for (i = 0; i < N; i++)
    {
      if (M - a[i] < a_min)
        continue;
      for (j = i + 1; j < N; j++)
      {
        temp = a[i] + a[j];
        if (temp <= M && temp > res)
          res = temp;
      }
    }
    if (res)
      printf("#%d %d\n", test_case, res);
    else
      printf("#%d %d\n", test_case, -1);
	}
	return 0;
}