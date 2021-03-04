#include <stdio.h>
int main(void)
{
	int test_case;
	int T, s, s_max, s_min;
  char temp;
	
	scanf("%d", &T);
  scanf("%c", &temp);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
    s = 0;
    s_max = 0;
    s_min = 64;
		while (1)
    {
      scanf("%c", &temp);
      if (temp == ' ' || temp == '\n')
      {
        if (s == 0 && temp == ' ')
          continue;
        if (s > s_max)
          s_max = s;
        if (s < s_min)
          s_min = s;
        s = 0;
        if (temp == '\n')
          break;
      }
      else
        s += (temp - '0');
    }
      printf("#%d %d %d\n", test_case, s_max, s_min);
	}
	return 0; 
}