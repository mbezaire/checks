import java.lang.reflect.Method;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.io.StringWriter;
import java.lang.reflect.*;
import java.util.Arrays;
import java.util.ArrayList;


public class Tester {
    static ArrayList<Check> checks = new ArrayList<Check>();
      public static void main(String[] args) throws IOException {
        Check one = new Check("constructors", 1, 3);

        try {
            BankAccount first = new BankAccount();
            BankAccount second = new BankAccount("Aaliyah");
            BankAccount third = new BankAccount("Anwar",55);
        } catch (Exception e) {
            one.setRationale(getMsg(e));
            one.setHelp("Make sure you have 3 constructors as detailed in instructions");
            checks.add(one);
            closeJson();
            return;
        }

        one.setPass(true);
        one.setPrintme("Construct 3 BankAccounts using different argument lists");
        checks.add(one);

        BankAccount first = new BankAccount();
        BankAccount second = new BankAccount("Aaliyah");
        BankAccount third = new BankAccount("Anwar",55);

        // Check 3
        Check getters = new Check("getters", 1, 3);
        String badMethods = checkMethods("BankAccount", new String[]{"getName","getBalance","getPinNumber"});
        if (badMethods.length() > 0) {
            getters.setRationale("Your " + "BankAccount" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
            getters.setHelp("Add the listed methods to your class; ensure their names are spelled correctly.");
            checks.add(getters);
            closeJson();
            return;
        }

        // Object output = runMethod("BankAccount", first, "getPinNumber");
         getters.setFailStatus(0);
         getters.addCheck(((String)runMethod("BankAccount", first, "getName")).trim(), "");
        getters.addCheck("" + ((Double)runMethod("BankAccount", first, "getBalance")), "0.0");
        getters.addCheck(((Integer)runMethod("BankAccount", first, "getPinNumber")) + "", "1000 - 9999");
         if ( ((String)runMethod("BankAccount", first, "getName")).equals("") &&
         within(((Double)runMethod("BankAccount", first, "getBalance")), 0) &&
        Math.abs(((Integer)runMethod("BankAccount", first, "getPinNumber")) + 1) > 0) {
            getters.setPass(true);
            //System.out.println("We have getters for each field");
         } else {
           getters.setPrintme("Getters not returning the expected values for each field.");
           getters.setHelp("Make sure the defaults are set as instructed.");
         }
         checks.add(getters);


        // Check 4: id = correctval
        Check correctval = new Check("correctval", 0, 4);
        correctval.addCheck(((String)runMethod("BankAccount", second, "getName")), "Aaliyah");
        correctval.addCheck(((String)runMethod("BankAccount", third, "getName")), "Anwar");

        if ( ((String)runMethod("BankAccount", second, "getName")).equals("Aaliyah") &&
            ((String)runMethod("BankAccount", third, "getName")).equals("Anwar")  )
         //System.out.println("Names are good");
         correctval.setPass(true);
        else {
           correctval.setPrintme("getName is not returning the expected name in every case.  ");
           correctval.setHelp("Make sure the getters are correct and each constructor uses all its arguments to set appropriate fields.");
         }

        correctval.addCheck("" + ((Double)runMethod("BankAccount", second, "getBalance")), "0");
        correctval.addCheck("" + ((Double)runMethod("BankAccount", third, "getBalance")), "55.0");

         if (!(
            within(((Double)runMethod("BankAccount", second, "getBalance")), 0) &&
            within(((Double)runMethod("BankAccount", third, "getBalance")), 55.0)))
             {
            correctval.setPass(false);
            String pr = correctval.getPrintme();
            correctval.setPrintme(pr + "getBalance is not returning the expected balance in every case");
           correctval.setHelp("Make sure the getters are correct and each constructor uses all its arguments to set appropriate fields.");
         }
         checks.add(correctval);

         // Check 5v id = deposit
        Check deposit = new Check("deposit", 1, 3);
        badMethods = checkMethods("BankAccount", new String[]{"deposit","withdraw"});
        if (badMethods.length() > 0) {
            //System.out.println("Your " + "BankAccount" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
            closeJson();
            return;
        }
        deposit.setFailStatus(0);
        deposit.setPrintme("Deposit $3.50 into one account, $100 into the next, -$5 into the third");
        deposit.setHelp("Make sure negative amounts are not deposited and do not affect the balance");
        runMethod("BankAccount", first, "deposit", new Object[]{3.50});
        runMethod("BankAccount", second, "deposit", new Object[]{100});
        runMethod("BankAccount", third, "deposit", new Object[]{-5});

        deposit.addCheck("" + ((Double)runMethod("BankAccount", first, "getBalance")), "3.5");
        deposit.addCheck("" + ((Double)runMethod("BankAccount", second, "getBalance")), "100");
        deposit.addCheck("" + ((Double)runMethod("BankAccount", third, "getBalance")), "55");

         if (
            within(((Double)runMethod("BankAccount", first, "getBalance")), 3.5) &&
            within(((Double)runMethod("BankAccount", second, "getBalance")), 100.0) &&
            within(((Double)runMethod("BankAccount", third, "getBalance")), 55.0)

         )
            deposit.setPass(true);


                 checks.add(deposit);


         // Check 6 id = withdraw
        Check withdraw = new Check("withdraw", 1, 6);
        withdraw.setPrintme("Create three BankAccounts with 10 each, withdraw -3, 5, and 15. Below shows first the balances of all 3 accounts and then the amount withdrawn from each.");
        withdraw.setHelp("Make sure withdraw doesn't remove more than the balance from the account, ignores negative withdrawal amounts, and returns amount withdrawn");
         first = new BankAccount("Peter",10);
         second = new BankAccount("Wendy",10);
         third = new BankAccount("Tinker",10);



        double firstd, secondd, thirdd;
        Object firstDoubVal = runMethod("BankAccount", first, "withdraw", new Object[]{-3});
        if (firstDoubVal != null && firstDoubVal instanceof Double) {
            firstd = (Double)firstDoubVal;
            secondd = (Double)(runMethod("BankAccount", second, "withdraw", new Object[]{5}));
            thirdd = (Double)(runMethod("BankAccount", third, "withdraw", new Object[]{15}));
            withdraw.setFailStatus(0);
       } else {
            withdraw.setFailStatus(1);
            withdraw.setHelp("Make sure the withdraw method returns a double");
            withdraw.setRationale("Incorrect return type for withdraw method in BankAccount");
            checks.add(withdraw);
            closeJson();
            return;
        }

        withdraw.addCheck("" + ((Double)runMethod("BankAccount", first, "getBalance")), "10.0");
        withdraw.addCheck("" + ((Double)runMethod("BankAccount", second, "getBalance")), "5.0");
        withdraw.addCheck("" + ((Double)runMethod("BankAccount", third, "getBalance")), "0.0");
        withdraw.addCheck("" + firstd, "0.0");
        withdraw.addCheck("" + secondd, "5.0");
        withdraw.addCheck("" + thirdd, "10.0");

        if (
            within(((Double)runMethod("BankAccount", first, "getBalance")), 10.0) &&
            within(((Double)runMethod("BankAccount", second, "getBalance")), 5.0) &&
            within(((Double)runMethod("BankAccount", third, "getBalance")), 0.0) &&
            within(firstd, 0.0) && within(secondd, 5.0) && within(thirdd, 10.0)
         )
           withdraw.setPass(true);
           checks.add(withdraw);


         // Check 7 - tostring
         Check tostring = new Check("tostring", 0, 1);
        tostring.setPrintme("Making a new BankAccount with a name and a balance");
        tostring.setHelp("Make sure the toString includes the name, balance, and pin number");
         first = new BankAccount("Michael", 12.34);
         String check1 = Check.toString(first.toString());
          int firstPin = ((Integer)runMethod("BankAccount", first, "getPinNumber"))
        tostring.addCheck(check1, "something containing Michael, 12.34, and the pin number " + firstPin);

         if (check1.contains("Michael") && check1.contains("12.34") && check1.contains("" + firstPin))
            tostring.setPass(true);
            checks.add(tostring);

         // Check 8 - pinnumber
         Check pinnumber = new Check("pinnumber", 0, 6);
         pinnumber.setPrintme("Creating 3 BankAccounts and calling their getPinNumber method to check their pin numbers");
         pinnumber.setHelp("Ensure the pin numbers are unique, randomly assigned, don't change unexpectedly, and are 4 digits");
         second = new BankAccount();
         third = new BankAccount("John");
         int firstPin = (Integer)runMethod("BankAccount", first, "getPinNumber");
         int secondPin = (Integer)runMethod("BankAccount", second, "getPinNumber");
         int thirdPin = (Integer)runMethod("BankAccount", third, "getPinNumber");
         int firstPin2 = (Integer)runMethod("BankAccount", first, "getPinNumber");
        pinnumber.addCheck("" + firstPin, "between 1000 - 9999");
        pinnumber.addCheck("" + secondPin, "between 1000 - 9999");
        pinnumber.addCheck("" + thirdPin, "between 1000 - 9999");
        pinnumber.addCheck("" + firstPin2, "" + firstPin + " (stays same for an account)");
        pinnumber.addCheck(firstPin + ", " + secondPin + ", " + thirdPin, "all 3 different");
        pinnumber.addCheck(firstPin + ", " + secondPin + ", " + thirdPin, "random, not incrementing by a constant");

        if (firstPin >= 1000 && firstPin <= 9999 &&
            secondPin >= 1000 && secondPin <= 9999 &&
            thirdPin >= 1000 && thirdPin <= 9999
             && firstPin != secondPin && secondPin != thirdPin
              && firstPin != thirdPin &&
              (secondPin - firstPin) != (thirdPin - secondPin) && firstPin == firstPin2)
             pinnumber.setPass(true);

             checks.add(pinnumber);
        closeJson();
    }

    private static Method methodIn(Method[] m, String name) {
        for (int i = 0; i < m.length; i++) {
            if (m[i].getName().equals(name))
                return m[i];
        }
        return null;
    }

    public static String checkMethods(String cla, String[] methods) {
        String methodsNotWorking = "";
        try {
            Class c = Class.forName(cla);
            Method m[] = c.getDeclaredMethods();
            for (String meth : methods) {
                Method method = methodIn(m, meth);
                if (method==null) {
                    methodsNotWorking += meth + ", ";
                }
            }
        }
        catch (Throwable e) {
            System.err.println(e);
            return e.toString();
        }
        return methodsNotWorking;
    }

    public static Object runMethod(String cla, Object obj, String meth) {
        String methodsNotWorking = "";
        try {
            Class c = Class.forName(cla);
            Method m[] = c.getDeclaredMethods();
            Method method = methodIn(m, meth);
            if (method!=null) {
                Object res = method.invoke(c.cast(obj));
                return res;
            }
            else
                return null;
        }
        catch (Throwable e) {
            System.err.println(e);
            return null;
        }
    }

    public static Object runMethod(String cla, Object obj, String meth, Object[] params) {
        String methodsNotWorking = "";
        try {
            Class c = Class.forName(cla);
            Method m[] = c.getDeclaredMethods();
            Method method = methodIn(m, meth);
            if (method!=null) {
                Object res = method.invoke(c.cast(obj), params);
                return res;
            }
            else
                return null;
        }
        catch (Throwable e) {
            System.err.println(e);
            return null;
        }
    }


    private static boolean within(double one, double two) {
      return Math.abs(one - two) < 0.0001;
    }

    public static String getMsg(Error e) {
      StringWriter sw = new StringWriter();
      PrintWriter pw = new PrintWriter(sw);
      e.printStackTrace(pw);
      String msg = Check.toString(sw);
      return msg.substring(0,msg.indexOf("Tester.main")-5);
   }


    public static String getMsg(Exception e) {
      StringWriter sw = new StringWriter();
      PrintWriter pw = new PrintWriter(sw);
      e.printStackTrace(pw);
      String msg = Check.toString(sw);
      return msg.substring(0,msg.indexOf("Tester.main")-5);
   }


   public static void closeJson() throws IOException {
        //PrintWriter json = new PrintWriter(new File("results1.json"));

        PrintStream json = System.out;
        json.println("{\n\"tests\": [");

        int r = 0;
        for (Check result : checks) {
            json.print(result.print());
            r++;
            if (r < checks.size())
                json.println(",");
        }

        json.println("\n]}");
        //json.close();
        return;
   }

}

class Check {
    protected String[] expected;
    protected String[] actual;
    protected String help = "";
    protected boolean pass;
    protected int failStatus = 0; // 0: mismatch, 1: failure
    protected String printme = "";
    protected String checkId = "";
    protected String rationale = "";
    private int checksSoFar = 0;

   public String print() {
      String expect = "";
      String act = "";
      for (int i = 0; i < this.expected.length; i++) {
        expect += this.expected[i] + "\\n";
        act += this.actual[i] + "\\n";

      }
      String result = "{\"pass\": " + pass + ",\"actual\": \"" + act + "\",\"expected\": \"" + expect + "\",\"failStatus\": " + failStatus + ",\"checkId\": \"" + checkId + "\",\"help\": \"" + help + "\",\"printme\": \"" + printme + "\",\"rationale\": \"" + rationale + "\",\"visibility\": \"" + (true ? "visible" : "hidden" ) +  "\"}";
      return result; // toString(result);
    }


    public Check(String checkId, int failStatus, int numChecks) {
        this.checkId = checkId;
        this.failStatus = failStatus;
        expected = new String[numChecks];
        actual = new String[numChecks];
    }

    public int getFailStatus() {
        return failStatus;
    }

    public void setFailStatus(int failStatus) {
        this.failStatus = failStatus;
    }

    public boolean getPass() {
        return pass;
    }

    public void setPass(boolean f) {
        pass = f;
    }

    public String getCheckId() {
        return checkId;
    }

    public String[] getExpected() {
        return expected;
    }

    public void addCheck(String actual, String expected) {
        this.expected[checksSoFar] = expected;
        this.actual[checksSoFar] = actual;
        checksSoFar++;
    }

    public String getHelp() {return help;}
    public void setHelp(String h) { help = h;}

    public String getPrintme() {return printme;}
    public void setPrintme(String h) { printme = h;}

    public String getRationale() {return rationale;}
    public void setRationale(String h) { rationale = h;}

        public static String toString(Object word) {
      return toString(word.toString());
   }
    public static String toString(String word) {
      return word.replace("\\","\\\\").replace("\n", "\\n").replace("\r", "").replace("\f", "").replace("\t", "\\t").replace("\"","\\\"");
   }
}
