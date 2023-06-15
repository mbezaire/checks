import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner ear = new Scanner(System.in);
        int num = ear.nextInt();ear.nextLine();
        String units = ear.nextLine();
        Duration test = new Duration(num, units);
        System.out.println(test.getSeconds());
    }
}