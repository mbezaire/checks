import java.util.Scanner;

public class F7Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      double v = reader.nextDouble();
      Fraction dividend = new Fraction(v);      
      System.out.println(dividend);
   }
}