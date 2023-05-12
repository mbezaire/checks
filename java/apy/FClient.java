

public class FClient
{
   public static void main(String[] args)
   {
      Chapter7part1 Ch7 = new Chapter7part1();
      System.out.println(Math.abs(Ch7.calcSum(2) - 1.25) < 0.00001 && Math.abs(Ch7.calcSum(100) - 1.634983) < 0.00001);
   }
}
