#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, temp;
    int c[3];
    int p[3];
    int res[3];
    char current[9];
    char plan[9];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", current);
		scanf("%s", plan);
        
        c[0] = (current[0] - '0') * 10 + (current[1] - '0');
        c[1] = (current[3] - '0') * 10 + (current[4] - '0');
        c[2] = (current[6] - '0') * 10 + (current[7] - '0');
        
        p[0] = (plan[0] - '0') * 10 + (plan[1] - '0');
        p[1] = (plan[3] - '0') * 10 + (plan[4] - '0');
        p[2] = (plan[6] - '0') * 10 + (plan[7] - '0');
        
        temp = 0;
        for (i = 2; i >= 0; i--)
        {
            res[i] = p[i] - c[i] - temp;
            if (res[i] < 0)
            {
                temp = 1;
                if (i != 0)
                    res[i] += 60;
                else
                    res[i] += 24;
            }
            else
                temp = 0;
        }
        printf("#%d ", test_case);
        for (i = 0; i < 3; i++)
        {
            if (res[i] < 10)
                printf("0%d", res[i]);
            else
                printf("%d", res[i]);
            if (i < 2)
                printf(":");
        }
        printf("\n");
        
	}
	return 0;
}