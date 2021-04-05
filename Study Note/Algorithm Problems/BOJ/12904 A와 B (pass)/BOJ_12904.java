import java.util.*;

public class BOJ_12904 {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        String T = sc.nextLine();
        
        int len_s = S.length();
        int len_t = T.length();
        
        while(len_s < len_t)
        {
            if (T.charAt(len_t - 1) == 'B')
                T = (new StringBuffer(T.substring(0, --len_t))).reverse().toString();
            else
                T = T.substring(0, --len_t);
        }
        if (S.equals(T))
            System.out.println(1);
        else
            System.out.println(0);
    }
}