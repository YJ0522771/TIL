import java.util.*;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A, B;
        A = sc.nextLong();
	    B = sc.nextLong();

        int count = 1;
        while(B > A)
        {
            if(B % 10 == 1)
                B /= 10;
            else if(B % 2 == 1)
                break;
            else
                B /= 2;
            count++;
        }
        if (A == B)
            System.out.println(count);
        else
            System.out.println(-1);
    }
}