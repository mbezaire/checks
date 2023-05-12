import java.util.Scanner;

public class F4Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();
      int d = reader.nextInt();
      Fraction factor1 = new Fraction(n, d);
      
      n = reader.nextInt();
      d = reader.nextInt();
      Fraction factor2 = new Fraction(n, d);
      
      System.out.println(factor1.add(factor2));
   }
}

/*

@check50.check(compiles)
def subtract():
    """Fractions can be subtracted"""
    check50.run("javac F5Client.java").stdin("1 3 1 4").stdout("1/12\n").exit(0)
*/