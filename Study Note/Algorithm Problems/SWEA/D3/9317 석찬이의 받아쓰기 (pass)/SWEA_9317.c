#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, count, i;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
		char str1[N + 1];
    char str2[N + 1];
        
    scanf("%s", str1);
    scanf("%s", str2);
        
    count = 0;
    for (i = 0; i < N; i++)
      if (str1[i] == str2[i])
        count++;
        
    printf("#%d %d\n", test_case, count);
	}
	return 0;
}