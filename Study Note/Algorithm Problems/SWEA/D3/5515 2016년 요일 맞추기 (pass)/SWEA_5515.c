#include <stdio.h>
int main(void)
{
	int test_case;
	int T, m, d, i;
  int month[13] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int week[7] = {3, 4, 5, 6, 0, 1, 2};
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &m, &d);
		for (i = 1; i < m; i++) d += month[i];
    printf("#%d %d\n", test_case, week[d%7]);
	}
	return 0; 
}