import java.util.Scanner;

public class TestRandInt
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();     
      int u = reader.nextInt();     
      System.out.println(Custom.randInt(n, u));
   }
}
