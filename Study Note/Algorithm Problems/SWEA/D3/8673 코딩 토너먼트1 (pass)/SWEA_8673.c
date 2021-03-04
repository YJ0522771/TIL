#include <stdio.h>
int W[512];
int main(void)
{
	int test_case;
	int T, K, i, j, a1, a2;
  unsigned int res;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &K);
    res = 0;
    for (i = 0; i < (1 << (K - 1)); i++)
    {
      scanf("%d", &a1);
      scanf("%d", &a2);
      if (a1 >= a2)
      {
          W[i] = a1;
          res += (a1 - a2);
      }
      else
      {
          W[i] = a2;
          res += (a2 - a1);
      }
    }
    
    for (i = K - 1; i > 0; i--)
      for (j = 0; j < (1 << i); j += 2)
        {
          a1 = W[j];
          a2 = W[j + 1];
          if (a1 >= a2)
          {
            W[j / 2] = a1;
            res += (a1 - a2);
          }
        else
          {
            W[j / 2] = a2;
            res += (a2 - a1);
          }
        }
		printf("#%d %d\n", test_case, res);
	}
	return 0;
}