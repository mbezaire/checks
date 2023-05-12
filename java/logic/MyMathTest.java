import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
// https://pypi.org/project/check50-junit/
class MyMathTest {
  @Test
  public void getMax2() {
    int z = MyMath.max(1,2);
    assertEquals(2, z);
  }
  
  @Test
  public void getMax3() {
    int z = MyMath.max(1,2);
    assertEquals(2, z);
  }
}