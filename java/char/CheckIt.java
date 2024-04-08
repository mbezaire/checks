//import java.io.*;

public class CheckIt {
    public static void main(String[] args) { //} throws IOException {
        //File output = new File("output.txt");
        //PrintWriter out = new PrintWriter(output);
        char[] ch = new char[3];
        ch[0] = (char)((int)'A' + (int)(Math.random()*10));
        ch[1] = (char)((int)'K' + (int)(Math.random()*10));
        ch[2] = (char)((int)'U' + (int)(Math.random()*5));

        for (int i = 0; i < ch.length; i++)
            System.out.println((int)ch[i] + "\t" + Warmup.ascii(ch[i]));

        for (int i = 0; i < ch.length; i++)
            System.out.println(ch[i] + "\t" + Warmup.upper((char)((int)ch[i] + 32)) + "\t" + (Warmup.upper(ch[i])));

        for (int i = 0; i < ch.length; i++)
            System.out.println(ch[i] + "\t" + Warmup.lower((char)((int)ch[i] + 32)) + "\t" + (Warmup.lower(ch[i])));

        System.out.println(Warmup.explain());
        //out.close();
     }
}
