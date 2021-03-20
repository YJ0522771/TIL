#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, j, k, idx, state, count;
    int visit[9];
    char temp;
    char nums[10];
    char colors[10];
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", nums);
        scanf("%s", colors);
        for (i = 0; i < 8; i++)
        {
            idx = i;
            for (j = i + 1; j < 9; j++)
                if (nums[idx] > nums[j])
                    idx = j;
            temp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = temp;
            temp = colors[i];
            colors[i] = colors[idx];
            colors[idx] = temp;
        }
        count = 0;
        for (i = 0; i < 9; i++)
            visit[i] = 0;
        for (i = 0; i < 7; i++)
        {
            state = 0;
            if (visit[i])
                continue;
            for (j = i + 1; j < 8; j++)
            {
                if (visit[j] || colors[i] != colors[j])
                    continue;
                for (k = j + 1; k < 9; k++)
                {
                    if (visit[k] || colors[j] != colors[k])
                        continue;
                    if (nums[i] == nums[j] && nums[j] == nums[k])
                    	state++;
                    else if (nums[i] == nums[j] - 1 && nums[j] == nums[k] - 1)
                        state++;
                    if (state)
                    {
                        //printf("%d %d %d\n", i, j, k);
                        visit[i] = 1;
                        visit[j] = 1;
                        visit[k] = 1;
                        count++;
                        break;
                    }
                }
                if (state)
                break;
            }
        }
        
        printf("#%d ", test_case);
        if (count >= 3)
        	printf("Win\n");
        else
            printf("Continue\n");
        /*
        for (i = 0; i < 9; i++)
        {
            printf("%c %c\n", nums[i], colors[i]);
        }*/
	}
	return 0;
}