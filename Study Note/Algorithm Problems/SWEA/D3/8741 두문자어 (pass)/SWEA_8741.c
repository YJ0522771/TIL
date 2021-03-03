#include <stdio.h>
int main(void)
{
	int test_case;
	int T, state;
  char temp;
	
	scanf("%d", &T);
  scanf("%c", &temp);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		state = 1;
    printf("#%d ", test_case);
		scanf("%c", &temp);
    while (temp != '\n')
    {
      if (state)
      {
        printf("%c", temp - 'a' + 'A');
        state = 0;
      }
      else if (temp == ' ')
        state = 1;
      scanf("%c", &temp);
    }
    printf("\n");
	}
	return 0;
}