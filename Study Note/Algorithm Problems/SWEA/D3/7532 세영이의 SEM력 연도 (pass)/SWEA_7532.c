#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
    unsigned long int SEM[3];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%lu %lu %lu", &SEM[0], &SEM[1], &SEM[2]);
        
        while (!(SEM[0] == SEM[1]) || !(SEM[1] == SEM[2]))
        {
            
            if (SEM[0] <= SEM[1] && SEM[0] <= SEM[2])
                SEM[0] += 365;
            else if (SEM[1] < SEM[2])
                SEM[1] += 24;
            else
                SEM[2] += 29;
            //printf("%lu %lu %lu\n", SEM[0], SEM[1], SEM[2]);
        }
		printf("#%d %d\n", test_case, SEM[0]);
	}
	return 0;
}