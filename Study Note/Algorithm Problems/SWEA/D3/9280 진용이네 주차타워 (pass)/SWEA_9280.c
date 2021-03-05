#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M, i, j, cost, temp, state, f, t;
	
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
		int R[N];
		int car[N];
		int W[M];
		int index[M + 1];
		int wait[M];
		f = 0;
		t = 0;
		for (i = 0; i < N; i++)
		{
			scanf("%d", &R[i]);
			car[i] = 0;
		}
		for (i = 0; i < M; i++)
		{
			index[i] = 0;
			wait[i] = 0;
			scanf("%d", &W[i]);
		}
		index[M] = 0;
		cost = 0;
		for (i = 0; i < 2 * M; i++)
		{
  			scanf("%d", &temp);
			if (temp > 0)
			{
				if (index[0] < N)
				{
					car[index[0]] = temp;
					index[temp] = index[0];
					cost += (W[temp - 1] * R[index[0]]);
					state = 0;
					for (j = 0; j < N; j++)
						if (car[j] == 0)
						{
						  state = 1;
						  break;
						}
					if (state)
						index[0] = j;
					else
						index[0] = N;
				}
				else
				{
					wait[t] = temp;
					t++;
				}
			}
			else
			{
				temp *= -1;
				car[index[temp]] = 0;

				if (f < t)
				{
					car[index[temp]] = wait[f];
					index[wait[f]] = index[temp];
					cost += (W[wait[f] - 1] * R[index[wait[f]]]);
					f++;
				}
				else if (index[temp] < index[0])
					index[0] = index[temp];
				index[temp] = 0;
			}
		}
    	printf("#%d %d\n", test_case, cost);   
	}
	return 0; 
}
