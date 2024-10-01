public class Client {
    public static void main(String[] args) {
        double ans = ShapeArea.getCircleArea(1);
        ans += ShapeArea.getSphereArea(1);
        ans += ShapeArea.getRectangleArea(1,1);
        ans += ShapeArea.getTriangleArea(1,1,1);
        System.out.println(ans);
    }
}