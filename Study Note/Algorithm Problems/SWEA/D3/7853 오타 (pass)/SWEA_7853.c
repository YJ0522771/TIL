char string[1001];
#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i;
    unsigned long int m = 1e9 + 7;
    unsigned long int res;
    char last, cur, next;
	
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", &string);
        res = 1;
        i = 0;
        cur = string[i];
        next = string[i + 1];
        while (cur != '\0')
        {
            if (i == 0)
            {
                if (cur != next)
                	res *= 2;
            }
            else if (next == '\0')
            {
                if (cur != last)
                    res *= 2;
            }
            else 
            {
                if (last != next && last != cur && next != cur)
                	res *= 3;
                else if (!(last == next && next == cur))
                	res *= 2;
            }
            if (res >= m)
                res %= m;
            last = cur;
            cur = next;
            i++;
            next = string[i + 1];
        }
		printf("#%d %lu\n", test_case, res);
	}
	return 0;
}