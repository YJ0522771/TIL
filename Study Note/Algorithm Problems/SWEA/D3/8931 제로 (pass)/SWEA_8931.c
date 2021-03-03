#include <stdio.h>
int main(void)
{
	int test_case;
	int T, K, end, i, temp;
  int stack[100000];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &K);
    end = 0;
    for (i = 0; i < K; i++)
    {
      scanf("%d", &temp);
      if (temp == 0)
        end--;
      else
      {
        stack[end] = temp;
        end++;
      }
    }
    temp = 0;
		for (i = 0; i < end; i++)
      temp += stack[i];
    printf("#%d %d\n", test_case, temp);
	}
	return 0;
}