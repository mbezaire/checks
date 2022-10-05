// Dr Bezaire
// Oct 4 2022
// Pretend Color Class

public class Color
{
    public static Color	black = new Color();
    public static Color	BLACK = black;
    public static Color	blue = new Color(0,0,255);
    public static Color	BLUE = blue;
    public static Color	cyan = new Color(0,255,255);
    public static Color	CYAN = cyan;
    public static Color	DARK_GRAY = new Color(50,50,50);
    public static Color	darkGray = DARK_GRAY;
    public static Color	gray = new Color(128,128,128);
    public static Color	GRAY = gray;
    public static Color	green = new Color(0,255,0);
    public static Color	GREEN = green;
    public static Color	LIGHT_GRAY = new Color(176,176,176);
    public static Color	lightGray = LIGHT_GRAY;
    public static Color	magenta = new Color(255,0,255);
    public static Color	MAGENTA = magenta;
    public static Color	orange = new Color(255,128,0);
    public static Color	ORANGE = orange;
    public static Color	pink = new Color(255,200,200);
    public static Color	PINK = pink;
    public static Color	red = new Color(255,0,0);
    public static Color	RED = red;
    public static Color	white = new Color(255,255,255);
    public static Color	WHITE = white;
    public static Color	yellow = new Color(255,255,0);
    public static Color	YELLOW = yellow;

    private int r;
    private int g;
    private int b;

    public Color()
    { }

    public Color(int r, int g, int b)
    {
        setR(r);
        setG(g);
        setB(b);
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