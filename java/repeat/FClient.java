// Dr B - read and print file
import java.util.Scanner;
public class FClient
{
   public static void main(String[] args)
   {
      Repeat repeatTest = new Repeat();
      Scanner input = new Scanner(System.in);
      System.out.println(repeatTest.repeat(input.nextLine()));
   }
}
