import java.util.Scanner;

public class F1Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();
      int d = reader.nextInt();
      Fraction quarter = new Fraction(n, d);
      System.out.println(quarter);
   }
}