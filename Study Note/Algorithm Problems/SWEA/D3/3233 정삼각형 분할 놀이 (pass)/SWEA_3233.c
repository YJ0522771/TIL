#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
  unsigned long int A, B;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &A, &B);
		printf("#%d %lu\n", test_case, (A / B) * (A / B));
	}
	return 0; 
}