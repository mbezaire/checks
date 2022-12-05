import java.util.Scanner;

public class F1Client
{
   public static void main(String[] args)
   {
      Chapter7part1 Ch7 = new Chapter7part1();
      System.out.println(Math.abs(Ch7.nextAlgorithm(100) + .99) < 0.00000001 && 
                         Math.abs(Ch7.nextAlgorithm(5) - 0.8) < 0.00000001);
   }
}