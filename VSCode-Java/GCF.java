import java.util.Scanner;

public class GCF {
    public static void main(String[] args) {
        Scanner myscanner = new Scanner(System.in);
        System.out.print("First Integer: ");
        int firstint = myscanner.nextInt();
        System.out.print("Second Integer: ");
        int secondint = myscanner.nextInt();
        System.out.println(String.format("G.C.F. Of %d And %d Equals %d.", firstint, secondint, findgcf(firstint, secondint)));
        myscanner.close();
    }
    public static int findgcf(int n1, int n2) {
        if (n2 != 0) return findgcf(n2, n1%n2);
        else return n1;
    }
}
