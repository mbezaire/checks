import java.util.Scanner;

public class CClient {
    public static void main(String[] args) {
        Scanner ear = new Scanner(System.in);
        int num = ear.nextInt();ear.nextLine();
        String units = ear.nextLine();
        Duration test = new Duration(num, units);
        num = ear.nextInt();ear.nextLine();
        units = ear.nextLine();
        Duration other = new Duration(num, units);
        System.out.println(test.isLonger(other) + "\n" + test.isLonger(test) + "\n" + other.isLonger(test));
    }
}