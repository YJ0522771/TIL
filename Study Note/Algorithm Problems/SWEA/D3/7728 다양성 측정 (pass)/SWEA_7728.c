#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, res;
    char num[15];
    int count[10];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", num);
		for (i = 0; i < 10; i++)
            count[i] = 0;
        i = 0;
        while (num[i] != '\0')
        {
            count[num[i] - '0']++;
            i++;
        }
        res = 0;
        for (i = 0; i < 10; i++)
            if (count[i])
                res++;
        printf("#%d %d\n", test_case, res);
	}
	return 0;
}