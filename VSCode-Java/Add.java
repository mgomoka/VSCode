import java.util.Scanner;

public class Add {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter First Number: ");
        double firstNumber = sc.nextDouble();
        System.out.print("Enter Second Number: ");
        double secondNumber = sc.nextDouble();
        double total = firstNumber + secondNumber;
        System.out.println("The Total Equals: " + total);
    }
}
