import java.util.Scanner;

public class CClient {
    public static void main(String[] args) {
        Scanner ear = new Scanner(System.in);
		System.out.println("Enter somethin");

        int num = ear.nextInt();ear.nextLine();
        String units = ear.nextLine();
        Duration test = new Duration(num, units);
		System.out.println("Enter somethin");

        num = ear.nextInt();ear.nextLine();
        units = ear.nextLine();
        Duration other = new Duration(num, units);
        Duration longer = test.addTime(other);
        System.out.println(longer + "\n" + longer.getTimeNumber() + " " + longer.getTimeUnits());
    }
}