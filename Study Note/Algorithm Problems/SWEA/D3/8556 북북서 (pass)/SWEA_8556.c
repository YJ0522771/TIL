#include <stdio.h>
char str[101];
char stack[20];
int main(void)
{
	int test_case;
	int T, count, i, dir, d;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", str);
    i = 0;
    count = 0;
    while (str[i] != '\0')
    {
        if (str[i] == 'n')
        {
            stack[count] = 'n';
            count++;
            i += 5;
        }
        else if (str[i] == 'w')
        {
            stack[count] = 'w';
            count++;
            i += 4;
        }
    }
    d = 1 << (count - 1);
    if (stack[count - 1] == 'n')
      dir = 0;
    else
      dir = 90 * d;      
    for (i = count - 2; i >= 0; i--)
    {
      if (stack[i] == 'n')
        dir -= (90 * (1 << i));
      else
        dir += (90 * (1 << i));
    }
    
    while (dir % 2 == 0 && d != 1)
    {
      dir /= 2;
      d /= 2;
    }
    if (d == 1)
      printf("#%d %d\n", test_case, dir); 
    else
      printf("#%d %d/%d\n", test_case, dir, d); 
	}
	return 0;
}