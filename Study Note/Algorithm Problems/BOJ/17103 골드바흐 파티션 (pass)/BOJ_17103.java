import java.util.*;

public class BOJ_17103 {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 초기값 false
        boolean[] is_p = new boolean[1000000];
        ArrayList<Integer> primes = new ArrayList<Integer>();
        // 전부 true로 채우기
        Arrays.fill(is_p, true);
        is_p[0] = false;
        is_p[1] = false;
        
        for(int i = 2; i < 1000000; i++)
        {
        	if(is_p[i])
        	{
        		primes.add(i);
        		for(int j = 2*i; j < 1000000; j += i)
        			is_p[j] = false;
        	}
        }
        
        int T = sc.nextInt();
        for (int test = 0; test < T; test++)
        {
        	int N = sc.nextInt();
        	int bk = N / 2 ;
        	int count = 0;
        	for (int p : primes)
        	{
        		if(p > bk)
        			break;
        		if(is_p[N - p])
        			count++;
        	}
        	System.out.println(count);
        }
    }
}