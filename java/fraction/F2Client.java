import java.util.Scanner;

public class F2Client
{
   public static void main(String[] args)
   {

      Fraction dividend = new Fraction(1,3);
      Fraction divisor = new Fraction(1,4);
      
      System.out.println(dividend.divide(divisor));
   }
}

/*

@check50.check(compiles)
def multiply():
    """Fractions can be multiplied"""
    check50.run("javac F3Client.java").stdin("1 4 1 3").stdout("1/12\n").exit(0)


@check50.check(compiles)
def add():
    """Fractions can be added"""
    check50.run("javac F3Client.java").stdin("1 4 1 3").stdout("7/12\n").exit(0)


@check50.check(compiles)
def subtract():
    """Fractions can be subtracted"""
    check50.run("javac F3Client.java").stdin("1 3 1 4").stdout("1/12\n").exit(0)
*/