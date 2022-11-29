

public class FClient
{
   public static void main(String[] args)
   {
      Chapter7part1 Ch7 = new Chapter7part1();
      System.out.println(Math.abs(Ch7.calcSum(2) - 1.25) < 0.00001 && Math.abs(Ch7.calcSum(100) - 1.634983) < 0.00001);
   }
}

/*

// 150 2053, 120 2014, 130 2024
      
      System.out.println(product(5,9)==45);
      System.out.println(product(3,1)==3);
      System.out.println(product(13,4)==52);
      System.out.println(product(6,0)==0);
      System.out.println(product(0,4)==0);
      int m = 45, n = 6, quotient = 7, remainder = 3;
      String check1 = m + "/" + n +  " gives\nquotient: " + quotient + ", remainder: " + remainder;
      System.out.println(check1.equals(division(m,n)));
      
      m = 13; n = 30; quotient = 0; remainder = 13;
      String check2 = m + "/" + n +  " gives\nquotient: " + quotient + ", remainder: " + remainder;
      System.out.println(check2.equals(division(m,n)));
      
      m = 14; n = 7; quotient = 2; remainder = 13;
      String check3 = m + "/" + n +  " gives\nquotient: " + quotient + ", remainder: " + remainder;
      System.out.println(check3.equals(division(m,n)));
      
      System.out.println(Math.abs(nextAlgorithm(100) - .99) < 0.00000001);*/

    
@check50.check(runs)
def divide():
    """Fractions can be divided"""
    check50.run("javac F2Client.java").stdin("1 4 1 3").stdout("12/1\n").exit(0)


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