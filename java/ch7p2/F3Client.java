import java.util.Scanner;

public class F3Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);

      int n = reader.nextInt();
      System.out.println(Chapter7Part2.isPrime(n));
   }
}
