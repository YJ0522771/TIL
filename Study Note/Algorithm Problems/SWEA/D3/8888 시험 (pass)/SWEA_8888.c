#include <stdio.h>
#include <string.h>
int test_scores[2000];
char person_pass[2000][2000];		// i번째 사람의 정보
int person_pass_num[2000];	  // i번째 사람이 통과한 테스트 수
int person_score[2000];		 // i번째 사람의 점수

int main(void)
{
	int test_case;
	int T;
    int N, M, P, temp, i, j, s, r, c;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d %d", &N, &M, &P);
        
    for (i = 0; i < M; i++)
        test_scores[i] = 0;
        
    for (i = 0; i < N; i++)
    {
      s = 0;
      for (j = 0; j < M; j++)
      {
        getchar();
        temp = getchar();
        if (temp == '0')
        {
          test_scores[j]++;
          person_pass[i][j] = '0';
        }
        else
        {
          person_pass[i][j] = '1';
          s += 1;
        }
      }
      person_pass_num[i] = s;
    }
        
    for (i = 0; i < N; i++)
    {
        person_score[i] = 0;
        for (j = 0; j < M; j++)
            if (person_pass[i][j] == '1') 
                person_score[i] += test_scores[j];
    }

    s = person_score[P - 1];
    c = person_pass_num[P - 1];
    r = 0;
    for (i = 0; i < N; i++)
    {
        if (i == P - 1)
            continue;
        if (person_score[i] > s)
            r++;
        else if (person_score[i] == s && person_pass_num[i] > c)
            r++;
        else if (person_score[i] == s && person_pass_num[i] == c && i < P - 1)
            r++;
    }
            
		printf("#%d %d %d\n", test_case, s, ++r);

	}
	return 0;
}