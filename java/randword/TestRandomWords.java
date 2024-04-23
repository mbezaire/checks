import java.util.Scanner;

public class TestRandomWords
{
   public static void main(String[] args)
   {
      Scanner reader = new Scanner(System.in);
      
      String n = reader.nextLine();     
      System.out.println(RandomWord.getOneRandomWord(n));
   }
}
