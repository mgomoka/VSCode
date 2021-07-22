import java.util.*;

public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please Enter An Integer To Find Its Factorial: ");
        long userNum = sc.nextLong();
        long factNum = findfactorial(userNum);
        System.out.println("The Factorial of " + userNum + " Is Equal To: " + factNum);
        sc.close();
    }
    public static long findfactorial(long num) {
        if(num >= 1){
            return num * findfactorial(num - 1);
        }
        else {
            return 1;
        }
    }
}
