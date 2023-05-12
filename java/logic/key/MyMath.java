/* Starter code for Chapter 6 exercises
   Complete the methods below.
   
   Dr. Bezaire - November 2022
*/
import java.util.Scanner;

public class MyMath
{
   public static int max(int x, int y)
   {
      // Write this max method so that it returns whichever is greater
      // between x and y (or either of them if equal). Do NOT use the
      // Math class for this exercise
      if (x > y)
         return x;
      return y;

   }

   public static int max(int x, int y, int z)
   {
      // Write this max method so that it returns whichever is greatest
      // among x, y and z (or any of them if equal). You may call your
      // other max method within this method if you like (not necessary).
      
      return max(max(x,y),z);
   }
   
   public static boolean isPerfectSquare(int x)
   {
      // Write this method to return true for a number that is a perfect
      // square and false for  other numbers (1, 4, 9 are true; 2, 5 are false).
      // Do NOT use loops or recursion. Use Math.sqrt, Math.round, and 
      // multiplication with boolean logic to figure this one out.
      
      int y = (int)Math.round(Math.sqrt(x));
      return y*y == x;
   }

   public static double totalWages(double hours, double rate)
   {
      double wages;
      // Write a method that computes total earnings for a week based on
      // the number of hours worked and the hourly rate. The pay for
      // overtime (hours worked over 40) is 1.5 times the regular rate.
      // For example, totalWages(42, 12.50) should return 593.75
      
      double extra = 0;
      if (hours > 40)
      {
         extra = hours - 40;
         hours -= extra;
      }
      
      return hours * rate + extra * rate * 1.5;
   }

   // Invent 3 unique ways to implement the concept of
   // XOR in Java. XOR is an operation that returns
   // true when one and only one of two conditions
   // is true. Implement one each in xor1, xor2, and
   // xor3 below:
   public static boolean xor1(boolean one, boolean two)
   {
      return !(one && two) && (one || two);
   }

   public static boolean xor2(boolean one, boolean two)
   {
      return (one && !two) || (!one && two);
   }

   public static boolean xor3(boolean one, boolean two)
   {
      return one != two;
   }
       
   public static boolean isGeometricSequence(int a, int b, int c)
   {
      // Write this method so that it tests if a, b, and c form
      // a geometric sequence. That is, a, b, and c are not
      // equal to 0 and a/b = b/c.
      // Hint: recall that comparing doubles using == may not
      // work; in this case you can use integer cross products
      // instead
   
      return a*b*c != 0 && a*c == b*b;
   }

   public static char getGrade(int avg)
   {
      // Rewrite this method so that the only relational operator
      // it uses is '<'. Logic should still work the same after
      // rewrite.
         
      if (avg < 60)
         return 'F';
      else if ( avg < 70)
         return 'D';
      else if (avg < 80)
         return 'C';
      else if (avg < 90)
         return 'B';
      else
         return 'A';
   
   }
   
   public static boolean isLater(int month1, int day1, int year1,
                                 int month2, int day2, int year2)
   {
      // This method should return true if the first date is
      // later than the second date and false otherwise
      
      if (year1 > year2)
         return true;
      else if (year1 < year2)
         return false;
      
      if (month1 > month2)
         return true;
      else if (month1 < month2)
         return false;
         
      return day1 > day2;
            
   }
   
   
   public static void main(String[] args)
   {
      // Test your code here
      
      int num1, num2, num3;
      int hoursWorked;
      double payRate;
      
      boolean test1, test2;
      
      // Date test:
      testDateCode();
   }
   
     public static void testDateCode()
  {
    Scanner kb = new Scanner(System.in);

    System.out.print("Enter the first date  (month day year): ");
    int month1 = kb.nextInt();
    int day1 = kb.nextInt();
    int year1 = kb.nextInt();

    System.out.print("Enter the second date (month day year): ");
    int month2 = kb.nextInt();
    int day2 = kb.nextInt();
    int year2 = kb.nextInt();

    kb.close();

    System.out.println();  // blank line

    String msg = month1 + "/" + day1 + "/" + year1;
    if (isLater(month1, day1, year1, month2, day2, year2))
      msg += " IS ";
    else
      msg += " is NOT ";
    msg += "later than " + month2 + "/" + day2 + "/" + year2;
    System.out.println(msg);
  }
}