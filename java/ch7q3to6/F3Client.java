import java.util.Scanner;

public class F3Client
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
      
      System.out.println(factor1.multiply(factor2));
   }
}

/*

@check50.check(compiles)
def add():
    """Fractions can be added"""
    check50.run("javac F4Client.java").stdin("1 4 1 3").stdout("7/12\n").exit(0)


@check50.check(compiles)
def subtract():
    """Fractions can be subtracted"""
    check50.run("javac F5Client.java").stdin("1 3 1 4").stdout("1/12\n").exit(0)
*/