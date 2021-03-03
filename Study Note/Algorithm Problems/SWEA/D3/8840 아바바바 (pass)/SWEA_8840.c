#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
  unsigned long int L;

	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%lu", &L);
		printf("#%d %lu\n", test_case, (L / 2) * (L / 2));
	}
	return 0;
}