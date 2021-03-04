#include <stdio.h>
int main(void)
{
	int test_case;
	int T, s, s_max, s_min, i;
  unsigned int temp;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
    s = 0;
    s_max = 0;
    s_min = 64;
        
    for (i = 0; i < 10; i++)
    {
      scanf("%d", &temp);
      while (temp > 0)
      {
        s += (temp % 10);
        temp /= 10;
      }
      if (s > s_max)
        s_max = s;
      if (s < s_min)
        s_min = s;
      s = 0;
    }
    printf("#%d %d %d\n", test_case, s_max, s_min);
	}
	return 0; 
}