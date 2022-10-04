// Dr Bezaire
// Oct 4 2022
// Pretend Color Class

public class Color
{
    public static Color	black = new Color();
    public static Color	BLACK = black;
    public static Color	blue = new Color(0,0,1);
    public static Color	BLUE = blue;
    public static Color	cyan = new Color(0,1,1);
    public static Color	CYAN = cyan;
    public static Color	DARK_GRAY = new Color(0.2,0.2,.2);
    public static Color	darkGray = DARK_GRAY;
    public static Color	gray = new Color(0.5,0.5,.5);
    public static Color	GRAY = gray;
    public static Color	green = new Color(0,1,0);
    public static Color	GREEN = green;
    public static Color	LIGHT_GRAY = new Color(0.7,0.7,.7);
    public static Color	lightGray = LIGHT_GRAY;
    public static Color	magenta = new Color(1,0,1);
    public static Color	MAGENTA = magenta;
    public static Color	orange = new Color(1,.5,0);
    public static Color	ORANGE = orange;
    public static Color	pink = new Color(1,.8,.8);
    public static Color	PINK = pink;
    public static Color	red = new Color(1,0,0);
    public static Color	RED = red;
    public static Color	white = new Color(1,1,1);
    public static Color	WHITE = white;
    public static Color	yellow = new Color(1,1,0);
    public static Color	YELLOW = yellow;

    private int r;
    private int g;
    private int b;

    public Color()
    { }

    public Color(int r, int g, int b)
    {
        this.r = setR(r);
        this.g = setG(g);
        this.b = setB(b);
    }

    public int getR()
    {
        return r;
    }

    public int getG()
    {
        return g;
    }

    public int getB()
    {
        return b;
    }

    public void setR(int r)
    {
        if (r <= 255 && r >= 0)
            this.r = r;
    }

    public void setG(int g)
    {
        if (g <= 255 && g >= 0)
            this.g = g;
    }

    public void setB(int b)
    {
        if (b <= 255 && b >= 0)
            this.b = b;
    }
    public String toString()
    {
        return "red: " + red + ", green: " + green + ", blue: " + blue;
    }
}