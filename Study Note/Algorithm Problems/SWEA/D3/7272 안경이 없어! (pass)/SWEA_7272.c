#include <stdio.h>
char one[6] = {'A', 'D', 'O', 'P', 'Q', 'R'};
int main(void)
{
	int test_case;
	int T, N, M, i, j, k, state;
    int test[2][20];
	char str[2][20];
    
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", str[0]);
        scanf("%s", str[1]);
        N = 0;
       	while (str[0][N] != '\0')
            N++;
        
        M = 0;
       	while (str[1][M] != '\0')
            M++;
        
        if (N != M)
        {
            printf("#%d DIFF\n", test_case);
            continue;
        }
        
        for (k = 0; k < 2; k++)
            for (i = 0; i < N; i++)
            { 
                if (str[k][i] == 'B')
					test[k][i] = 2;
                else 
                {
                    state = 1;
                	for (j = 0; j < 6; j++)
                    	if (str[k][i] == one[j])
                        {
                            state = 0;
                            test[k][i] = 1;
                            break;
                        }
                    if (state)
                        test[k][i] = 0;
                }
            }

        state = 1;
        for (i = 0; i < N; i++)
            if (test[0][i] != test[1][i])
                state = 0;
        if (state)
            printf("#%d SAME\n", test_case);
        else
            printf("#%d DIFF\n", test_case);
	}
	return 0;
}