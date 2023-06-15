import java.util.Scanner;

public class CBlient {
    public static void main(String[] args) {
        Scanner ear = new Scanner(System.in);
		System.out.println("Enter somethin");
        int num = ear.nextInt();
        String units = ear.nextLine();
        Duration test = new Duration(num, units.substring(1));
		System.out.println("Enter somethin");
        num = ear.nextInt();
        units = ear.nextLine();
        Duration other = new Duration(num, units.substring(1));
        System.out.println(test.isLonger(other) + "\n" + test.isLonger(test) + "\n" + other.isLonger(test));
    }
}