import java.util.Scanner;

public class TestRandInt
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();     
      int u = reader.nextInt();     
      int num = Custom.randInt(n, u);
      System.out.println(num);
   }
}
