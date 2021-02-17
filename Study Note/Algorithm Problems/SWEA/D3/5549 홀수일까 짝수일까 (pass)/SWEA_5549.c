#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, n;
    char *str;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", str);
		i = 0;
        while (str[i] != '\0')
            i++;
        n = str[i-1] - '0';
        if (n % 2) printf("#%d Odd\n", test_case);
        else printf("#%d Even\n", test_case);
	}
	return 0;
}