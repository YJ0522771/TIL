#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, max, temp, i, res;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
    res = 0;
    max = 0;
    for (i = 0; i < N; i++)
    {
      scanf("%d", &temp);
      res += temp;
      if (max < temp)
        max = temp;
    }
    printf("#%d %d\n", test_case, res + max + N);
	}
	return 0; 
}