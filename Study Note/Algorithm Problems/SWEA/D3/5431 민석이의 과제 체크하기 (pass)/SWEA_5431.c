#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, K, i, stu;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &K);
      int count[N];
      for (i = 0; i < N; i++) 
        count[i] = 0;
      for (i = 0; i < K; i++)
      {
        scanf("%d", &stu);
        count[--stu]++;
      }
      printf("#%d", test_case);
      for (i = 0; i < N; i++)
        if (!count[i])
          printf(" %d", i + 1);
      printf("\n");
	}
	return 0;
}