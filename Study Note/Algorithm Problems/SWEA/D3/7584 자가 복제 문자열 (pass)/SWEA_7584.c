#include <stdio.h>
#include <math.h>
int main(void)
{
	int test_case;
	int T, i, count;
    unsigned long int K, temp;
	
	scanf("%d", &T);
    
	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf("%lu", &K);
        count = 0;
        
        while (K > 1)
        {
            for (i = 0; i < 64; i++)
            {
                temp = pow(2, i);
                if (K <= temp)
                    break;
            }
            if (K == temp)
                break;
            K = temp - K;
            count++;
			//printf("%lu\n", K);
        }
        printf("#%d %d\n", test_case, count % 2);
	}
	return 0; 
}