#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i, j, temp, state, last, result;
	
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        int nums[N];
        for (i = 0; i < N; i++)
          scanf("%d", &nums[i]);
        state = 0;
        result = 0;
        for (i = 0; i < N - 1; i++)
        {
            for (j = i + 1; j < N; j++)
            {
             	temp = nums[i] * nums[j];
                last = temp % 10;
                temp = temp / 10;
                while (temp > 0)
                {
                    if ((last - 1) != (temp % 10))
                        break;
                    last = temp % 10;
                    temp = temp / 10;
                }
                if (temp <= 0) 
                {
                    state = 1;
                    if (result < nums[i] * nums[j])
                        result = nums[i] * nums[j];
                }
            }
        }
        if (state == 1) printf("#%d %d\n", test_case, result);
        else printf("#%d -1\n", test_case);

	}
	return 0;
}