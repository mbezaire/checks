import java.util.Scanner;

public class F0Client
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();
      int d = reader.nextInt();
      Chapter7part1 Ch7 = new Chapter7part1();
      
      Ch7.division(n,d);
   }
}
