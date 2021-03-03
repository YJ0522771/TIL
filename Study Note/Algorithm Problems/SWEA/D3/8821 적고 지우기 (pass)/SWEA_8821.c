#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, res;
  int note[10];
  char temp;
	
	scanf("%d", &T);
	scanf("%c", &temp);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%c", &temp);
    for (i = 0; i < 10; i++)
      note[i] = 0;
    while (temp != '\n')
    {
      if (note[temp - '0'])
        note[temp - '0']--;
      else
        note[temp - '0']++;
      scanf("%c", &temp);
    }
    res = 0;
    for (i = 0; i < 10; i++)
			res += note[i];
    printf("#%d %d\n", test_case, res);
	}
	return 0;
}