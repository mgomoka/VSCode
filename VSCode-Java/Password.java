import java.util.Scanner;

public class Password {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String totalpassword = "bazaar";
        
        System.out.print("Password:");
        String password = sc.nextLine();

        if(password.equals(totalpassword)) {System.out.println("Welcome");}
        else {System.out.println("Rejected");}

        sc.close();
    }
}
