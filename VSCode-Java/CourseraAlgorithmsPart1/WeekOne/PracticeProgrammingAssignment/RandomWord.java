package CourseraAlgorithmsPart1.WeekOne.PracticeProgrammingAssignment;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String inputstring = new String();
        String champion = new String();
        int i = 1;
        while(!StdIn.isEmpty()){
            inputstring = StdIn.readString();
            if(StdRandom.bernoulli(1.0/((double)i))){
                champion = inputstring;
            }
            i++;
        }
        StdOut.println("\n" + champion);
    }
}
