import java.util.Scanner;

public class F0Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();
      int d = reader.nextInt();
      Fraction factor1 = new Fraction(n, d);

      
      System.out.println(factor1.value());
   }
}
