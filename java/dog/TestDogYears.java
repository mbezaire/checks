import java.util.Scanner;

public class TestDogYears
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      int n = reader.nextInt();     
      System.out.println(Dog.dogYears(n));
   }
}
