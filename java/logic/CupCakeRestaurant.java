import java.util.Scanner;

public class CupCakeRestaurant
{
    public static void main(String[] args)
    {
        Scanner reader = new Scanner(System.in);
        PartyOrder one = new PartyOrder(reader.nextInt());
        PartyOrder two = new PartyOrder(reader.nextInt());
        one.setNumPeople(reader.nextInt());
        System.out.println(PartyOrder.getNumOrders() + " orders with " + PartyOrder.getTotalCupCakes() + " cupcakes.");
    }

}