import java.util.Scanner;

public class Quadrilateral {
    public static String type;
    public static int numberofsides;
    public static float sumofangles;
    public static float sidelengthone;
    public static float sidelengthtwo;
    public static float sidelengththree;
    public static float sidelengthfour;
    public static float angleone;
    public static float angletwo;
    public static float anglethree;
    public static float anglefour;

    public static void main(String[] args) {
        Scanner myscanner = new Scanner(System.in);
        type = myscanner.next();
        switch (type) {
            case "Quadrilateral":
                System.out.println("Quadrilateral");
                System.out.println("Enter Quadrilateral Dimensions");
                System.out.print("Top Side "); double quadtopside = myscanner.nextDouble();
                System.out.print("Left Side "); double quadleftside = myscanner.nextDouble();
                System.out.print("Bottom Side "); double quadbottomside = myscanner.nextDouble();
                System.out.print("Right Side "); double quadrightside = myscanner.nextDouble();
                System.out.print("Top Right Angle "); double quadtrangle = myscanner.nextDouble();
                System.out.print("Top Left Angle "); double quadtlangle = myscanner.nextDouble();
                System.out.print("Bottom Left Angle "); double quadblangle= myscanner.nextDouble();
                System.out.print("Bottom Right Angle "); double quadbrangle = myscanner.nextDouble();
                break;
            case "Trapezoid":
                System.out.println("Trapezoid");
                break;
            case "Isosceles Trapezoid":
                System.out.println("Isosceles Trapezoid");
                break;
            case "Parallelogram":
                System.out.println("Parallelogram");
                break;
            case "Rectangle":
                System.out.println("Rectangle");
                break;
            case "Rhombus":
                System.out.println("Rhombus");
                break;
            case "Square":
                System.out.println("Square");
                break;
            default:
                System.out.println("Default");
                break;
        }
        myscanner.close();
    }
}
