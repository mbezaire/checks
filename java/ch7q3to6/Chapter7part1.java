// Java Chapter 7 questions 3 - 6
import java.util.Scanner;

public class Chapter7part1
{
   // Write a method named calcSum to calculate and return the sum
   // 1/(1*1) + 1/(2*2) + 1/(3*3) + .... + 1/(n*n)
   // given a integer parameter n

   public static double calcSum(int n)
   {
      double sum = 0;
      for(int i = 1;i<=n;i++){
         sum+=1.0/(double)(i*i);
      }
      return sum;
   }

   // Then complete this method closeNpi that computes
   // how close the sum for n = 10000 is to pi*pi / 6. Return
   // how close the two are:

   public static double closeNpi(int n)
   {
      double sum = Math.abs((calcSum(10000)) - ((Math.PI*Math.PI)/6));
      return sum;
   }

   // Write a method called nextAlgorithm that
   // calculates the sum of the following
   // algorithm given an input n:
   // 1 - 1 / 2 + 1 / 3 - .... + (or - ) 1 / n
   // for any given n. 1 / k is added to the
   // sum if k is odd and 1 / k is subtracted
   // from the sum if k is even.

   public static double nextAlgorithm(int n)
   {
      double sum = 0;
      int i = 1;
      while(i<n){
	      if (i%2 == 0){
		      sum = sum - (1/i);
            i++;
         }else{
		      sum = sum + (1/i);
            i++;
         }
      }
      return sum;
   }


   // These sums converge to ln (2), the natural
   // log of 2. Add a calculation to your program
   // that computes how close the sum for
   // n = 10000 is to Math.log(2)
   public static double closeNlog(int n)
   {
      double sum = Math.abs(10000.0 - n);
      double answer = Math.abs(sum - Math.log(2));
      return answer;
   }


   // Write a method that returns the product
   // without using multiplication. You should
   // use an iterative strategy in this method.
   // You can assume that a >= 0 and b >= 0
   // (so a precondition is a >= 0 and b >= 0)
   public static int product(int a, int b)
   {
      int answer = 0;
      for(int i = 0; i<b; i++){
         answer+=a;
      }
      return answer;
      // ...

   }


   // Design an iterative strategy that,
   // given two integers m and n, calculates
   // the integer quotient and the remainder
   // when m is divided by n. Your algorithm
   // can use only +, -, and comparison
   // operations for integers. Implement your
   // algorithm in this division method:
   public static void division(int m, int n)
   {
      int quotient = 0;
      int originalM = m;
      // ...
      // m / n
      // 10 / 2
      // 11 / 2
      while(m-n>=0){
         m=m-n;
         quotient++;
      }
      int remainder = m;

      System.out.println(originalM + "/" + n + " gives\n" + "quotient: " + quotient + ", remainder: " + remainder);

   }

   // The population of Mexico at the end of 2014 was around
   // 123.8 million. Write and test a program that will prompt
   // the user for a number (a double) that represents the target
   // population number (in millions) and print out the year in
   // which the population of Mexico will reach or exceed that
   // number, assuming a constant growth rate of 0.5 percent per
   // year.
   // Declare the starting year (2014), the starting population
   // number (123.8), and the growth rate (0.5 percent) as
   // symbolic constants.
   public static void populationMexico()
   {
      Scanner reader = new Scanner(System.in);
      System.out.println("\nTarget population number in millions: ");
      int targ = reader.nextInt();
      int year = 2014;
      double growth = 1.005;
      double starting = 123.8;

      while(starting<targ){
         starting *= growth;
         year++;
      }

      System.out.println(year);
   }

   public static void main(String[] args)
   { // use this to test your code
     // Add more tests to test your sum algorithms
     // and how close they are to the approximations
     // given above

      Scanner reader = new Scanner(System.in);

      System.out.println("\nThe sum when you input 2 is: " + calcSum(2)+ " \n100: " + calcSum(100));

      System.out.println("\nThe closeness to pi^2/6 when you input 2 is: " + closeNpi(2));

      System.out.println("\nThe sum of the algorithm given the input of 2 is: " + nextAlgorithm(2));

      System.out.println("\nThe closeness of the sum for n=10000 when n is 2 to log 2 is: " + closeNlog(2));

      division(10,2);


      System.out.println("populationMexico(350)");
   }
}