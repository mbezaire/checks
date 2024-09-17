import java.util.Scanner;

public class OrderClient
{
    public static void main(String[] args)
    {
	Scanner ear = new Scanner(System.in);
        ClassCopies apJavaQuiz = new ClassCopies(0,0);

        apJavaQuiz.setNumStudents(ear.nextInt());

        apJavaQuiz.setNumPagesPerHandout(ear.nextInt());

        System.out.println(apJavaQuiz);

    }
}