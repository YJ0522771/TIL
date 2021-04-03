import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 초기값 0
        int[] path = new int[100001];
        Arrays.fill(path, -1);
        ArrayList<Integer> q = new ArrayList<Integer>();
        ArrayList<Integer> t = new ArrayList<Integer>();
        
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        path[N] = 0;
        q.add(N);
        t.add(0);
        int nq, nt = 0;
        while(!q.isEmpty())
        {
        	nq = q.remove(0);
        	nt = t.remove(0);
        	
        	if(nq == K)
        		break;
        	
    		int[] arr = {nq + 1, nq - 1, 2 * nq};
    		for(int a : arr)
    			if(a < 100001 && a >= 0 && path[a] == -1)
    			{
    				path[a] = nt + 1;
    				q.add(a);
    				t.add(nt + 1);
    			}    
        }
        System.out.println(nt);
    }
}