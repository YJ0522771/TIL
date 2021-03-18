#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i;
    char s[40];
    char count[26];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 0; i < 26; i++)
            count[i] = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%s", s);
            count[s[0] - 'A']++;
        }
        for (i = 0; i < N; i++)
            if (!count[i])
                break;
        printf("#%d %d\n", test_case, i);
	}
	return 0;
}