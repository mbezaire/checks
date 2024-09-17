import java.util.Scanner;

public class SuperClient
{
    public static void main(String[] args)
    {
	Scanner ear = new Scanner(System.in);
        ClassCopies apJavaQuiz = new ClassCopies(ear.nextInt(),ear.nextInt());
        PrintOrder worksheet = new PrintOrder(ear.nextInt());
        System.out.println("Total pages: " + PrintOrder.getTotalPages());

    }
}