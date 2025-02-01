import java.util.Scanner;
import java.util.Arrays;

public class TestSplit {
    public static void main(String[] args) {
        Scanner ear = new Scanner(System.in);
        String phrase = ear.nextLine();
        String del = ear.nextLine();
        char delim = del.charAt(0);
        String[] arr = Split.split(phrase,delim);
        System.out.println(Arrays.toString(arr) + "\nLength: " + arr.length);
    }
}