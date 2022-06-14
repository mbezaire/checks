import java.util.Scanner;

public class F1Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      System.out.println("Enter the numerator:");
      int n = reader.nextInt();
      System.out.println("Enter the denominator:");
      int d = reader.nextInt();
      Fraction quarter = new Fraction(n, d);
      System.out.println(quarter);
   }
}