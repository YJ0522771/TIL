#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, N, x, j, zero, res;
  int temp[26];

	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
    scanf("%d", &N);
		char count[N][26];
    char word[101];
    for (x = 0; x < N; x++)
	    for (i = 0; i < 26; i++)
        count[x][i] = 0;
        
    for (x = 0; x < N; x++)
    {
      scanf("%s", word);
      i = 0;
      while (word[i] != '\0')
      {
        count[x][word[i] - 'a']++;
        i++;
      }
    }
    res = 0;
    for (x = 0; x < (1 << N); x++)
    {
      for (i = 0; i < 26; i++)
        temp[i] = 0;
      for (i = 0; i < N; i++)
        if (x & (1 << i))
          for (j = 0; j < 26; j++)
            temp[j] += count[i][j];
      zero = 0;
      for (i = 0; i < 26; i++)
        if (temp[i] == 0)
          zero++;
      if (zero == 0)
        res++;
    }
    printf("#%d %d\n", test_case,  res);
	}
	return 0;
}