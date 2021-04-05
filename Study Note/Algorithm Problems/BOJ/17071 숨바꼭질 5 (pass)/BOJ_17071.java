import java.util.*;

public class BOJ_17071 {
	static Scanner sc = new Scanner(System.in);
    // 초기값 0
    static int[][] path = new int[2][500001];
    static Queue <Integer> q = new LinkedList<>();
	public static void main(String[] args) {
		Arrays.fill(path[0], -1);
		Arrays.fill(path[1], -1);
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        path[0][N] = 0;
        q.add(N);
        int time = 0;
        while(K <= 500000)
        {
        	int state = time % 2;
        	if(path[time % 2][K] != -1 && time >= path[time % 2][K])
				break;

        	time++;
        	state = time % 2;
        	Queue <Integer> nq = new LinkedList<>();
        	while(!q.isEmpty())
        	{
        		int cur = q.poll();
        		int[] arr = {cur + 1, cur - 1, 2 * cur};
        		for(int a : arr)
        			if(a < 500001 && a >= 0 && path[state][a] == -1)
        			{
        				path[state][a] = time;
        				nq.add(a);
        			}    
        	}
        	q = nq;
        	K += time;
        }

        if(K > 500000)
        	System.out.println(-1);
        else
        	System.out.println(time);
    }
}