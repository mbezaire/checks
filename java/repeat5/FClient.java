// Dr B - read and print file
import java.util.Scanner;
public class FClient
{
   public static void main(String[] args)
   {
      Repeat5 repeatTest = new Repeat5();
      Scanner input = new Scanner(System.in);
      System.out.println(repeatTest.repeat5(input.nextLine()));
   }
}
