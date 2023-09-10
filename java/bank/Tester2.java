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


public class Tester2 {
    static ArrayList<Check> checks = new ArrayList<Check>();
      public static void main(String[] args) throws IOException {

         // Check 9
         // Check that Bank is there and compiles and is longer than 17 lines
         // done entirely in the py check file

         // Check 10 - bankstruct: Bank can be created with a specific name and room for 3
        Check bankstruct = new Check("bankstruct", 1, 1);
        bankstruct.setPrintme("Making Bank(s) and checking for public MAX_ACCOUNTS field set to 3");
         try {
            //Bank local = new Bank("Reading Coop");
            Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");
         } catch (Error e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure you have defined a Bank class and have no syntax errors");
            checks.add(bankstruct);
            closeJson();
            return;
         } catch (ClassNotFoundException e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure you have defined a Bank class");
            checks.add(bankstruct);
            closeJson();
            return;
         }catch (NoSuchMethodException e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure you have a Bank constructor with the correct parameter list as detailed in the instructions");
            checks.add(bankstruct);
            closeJson();
            return;
         }catch (InstantiationException e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure you have properly declared the MAX_ACCOUNTS field as detailed in instructions");
            checks.add(bankstruct);
            closeJson();
            return;
         }catch (IllegalAccessException e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure your method logic and visibility modifiers are correct");
            checks.add(bankstruct);
            closeJson();
            return;
         }catch (Exception e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure you have a Bank constructor and properly declared fields as detailed in instructions");
            checks.add(bankstruct);
            closeJson();
            return;
         }
          try {
            String badFields = checkFields("Bank", new String[]{"name","MAX_ACCOUNTS","numAccounts"});
            Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");

            if (badFields.length() > 0) {
                bankstruct.setRationale("Your " + "Bank" + " class is missing these fields: " + badFields.substring(0, badFields.length()-2));
                bankstruct.setHelp("Add the listed fields to your class; ensure their names are spelled correctly and visibility set as instructed.");
                checks.add(bankstruct);
                closeJson();
                return;
            }
            else if (localClass.getField("MAX_ACCOUNTS").getInt(local) != 3) {
                bankstruct.setFailStatus(0);
                bankstruct.addCheck("" + localClass.getField("MAX_ACCOUNTS").getInt(local), "3");
                bankstruct.setRationale("Your " + "MAX_ACCOUNTS" + " variable in the Bank class should be set to 3");
                bankstruct.setHelp("Add the listed fields to your class; ensure their names are spelled correctly and visibility set as instructed.");
                checks.add(bankstruct);
                closeJson();
                return;
            }
         } catch (Exception e) {
            bankstruct.setRationale(getMsg(e));
            bankstruct.setHelp("Make sure your Bank class has the right fields and that any constants are public");
            checks.add(bankstruct);
            closeJson();
            return;
         }
         bankstruct.setPass(true);
         bankstruct.setPrintme("Construct a Bank with room for 3 accounts only");
         checks.add(bankstruct);

         // Check 11 - account3: Accounts are kept track of correctly, without using arrays (that check is in Python),
         //          and up to 3 can be created
        Check account3 = new Check("account3", 1, 1);
        try {
        String badMethods = checkMethods("Bank", new String[]{"addAccount"});
        if (badMethods.length() > 0) {
            account3.setRationale("Your " + "Bank" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
            account3.setHelp("Add the listed methods to your class; ensure their names are spelled correctly.");
            checks.add(account3);
            closeJson();
            return;
        }
        } catch (Exception e) {
            account3.setRationale(getMsg(e));
            account3.setHelp("Make sure you have all the methods for Bank as detailed in instructions");
            checks.add(account3);
            closeJson();
            return;
        }


       try {
        account3.setPrintme("Making 3 accounts and trying to make a 4th");
        account3.setHelp("Allow space for 3 BankAccounts in Bank and no more");
                    Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");

            int pin1 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name1", 50});
            int pin2 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name2", 50});
            int pin3 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name3", 50});
            int pin4 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name4", 50});
            if (pin4 <= 0 && (pin1 > 0 && pin2 > 0 && pin3 > 0))
                account3.setPass(true);
            else {
                account3.setRationale("Checked for 3 calls to addAccount that return real pin numbers and a 4th that returns 0 or less and doesn't make the account, but got these pins: " +
                                     pin1 + ", " + pin2 + ", " + pin3 + ", " + pin4);
                checks.add(account3);
                closeJson();
                return;
            }
        } catch (Exception e) {
            account3.setRationale(getMsg(e));
            checks.add(account3);
            closeJson();
            return;
        }
        account3.setFailStatus(0);
         account3.setPrintme("Add up to 3 BankAccounts at the Bank");
        checks.add(account3);


         // Check 12 - view: Accounts can be found and viewed if the correct information is provided (and not otherwise)
       Check accountview = new Check("accountview", 1, 0);
        try {
        String badMethods = checkMethods("Bank", new String[]{"showAccount", "findAccount"});
        if (badMethods.length() > 0) {
            accountview.setRationale("Your " + "Bank" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
            accountview.setHelp("Add the listed methods to your class; ensure their names are spelled correctly.");
            checks.add(accountview);
            closeJson();
            return;
        }
        } catch (Exception e) {
            accountview.setRationale(getMsg(e));
            accountview.setHelp("Make sure you have all the methods for Bank as detailed in instructions");
            checks.add(accountview);
            closeJson();
            return;
        }
         accountview.setFailStatus(0);

       try {
        accountview.setPrintme("View an account after adding, only with correct name and pin");
        accountview.setHelp("Make sure the showAccount method only shows account info if the name and pin match what the user provides");
                    Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");

            int pin1 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name1", 50});
            int pin2 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name2", 50});
            int pin3 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name3", 59.99});
            String acctInfo = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name3", pin3});
            String noAcctInfo = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name4", pin3});
            String alsoNoAcctInfo = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name3", pin3 - 1});

            if (!((noAcctInfo == null || noAcctInfo.equals("")) &&
                (alsoNoAcctInfo == null || alsoNoAcctInfo.equals("")))) {
                    accountview.setFailStatus(1);
                    accountview.setRationale("Unauthorized BankAccount access");
                    accountview.setHelp("Make sure you check that both the name and the pin match. If they don't, return an empty String or null.");
                    accountview.setPrintme("View an account after adding, only with correct name and pin\nFor Name3 (" + pin3 + "), we get: " + acctInfo
                                            + "\nFor Name4 (" + pin3 + "), we get: " + noAcctInfo
                                            + "\nFor Name3 (" + (pin3 - 1) + "), we get: " + alsoNoAcctInfo
                                            );
                    checks.add(accountview);
                    closeJson();
                    return;
                }
            else if (acctInfo != null && acctInfo.contains("Name3") && acctInfo.contains("" + pin3)) {
                if ( acctInfo.contains("59.99")) {
                    accountview.setPass(true);
                    accountview.setPrintme("View account details with proper validation");
                } else  {
                accountview.setFailStatus(1);
               accountview.setRationale("BankAccount was viewable but didn't seem to contain the correct balance in the toString (59.99):\n" + acctInfo);
                    accountview.setHelp("Make sure the balance of your BankAccount is correct after depositing and withdrawing. Also ensure your toString correctly reports the balance.");
                }
                }
            else {
                accountview.setFailStatus(1);
               accountview.setRationale("BankAccount not viewable " + (acctInfo != null) + acctInfo.contains("Name3") + acctInfo.contains("" + pin3));
               //accountview.setPrintme("View an account after adding, only with correct name and pin\nFor Name3 (" + pin3 + "), we get: " + acctInfo);
                accountview.setHelp("Make sure you check that the name and the pin match (and use String methods for the name check). If they do match, show the account name, pin, and balance.");
                checks.add(accountview);
                closeJson();
                return;
            }
        } catch (Exception e) {
           accountview.setFailStatus(1);
            accountview.setRationale(getMsg(e));
            checks.add(accountview);
            closeJson();
            return;
        }
        checks.add(accountview);

         // Check 13 - bankmethod: Accounts can be deposited into and withdrawn from
                Check depdraw = new Check("depdraw", 1, 0);
        try {
        String badMethods = checkMethods("Bank", new String[]{"deposit", "withdraw"});
        if (badMethods.length() > 0) {
            depdraw.setRationale("Your " + "Bank" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
            depdraw.setHelp("Add the listed methods to your class; ensure their names are spelled correctly.");
            checks.add(depdraw);
            closeJson();
            return;
        }
        } catch (Exception e) {
            depdraw.setRationale(getMsg(e));
            depdraw.setHelp("Make sure you have all the methods for Bank as detailed in instructions");
            checks.add(depdraw);
            closeJson();
            return;
        }
         depdraw.setFailStatus(0);


       try {
        depdraw.setPrintme("The withdraw and deposit methods must change the balance accurately, when given a reasonable input value");
        depdraw.setHelp("Make sure the withdraw and deposit methods only allow positive amounts to change the balance and that withdraw doesn't allow the account to be overdrawn");
            Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");

            int pin1 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name1", 50});
            int pin2 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name2", 50});
            int pin3 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name3", 100});
            double shTrue1 = (double)runMethod("Bank", local, "withdraw", new Object[]{"Name1", pin1, 10.50});
            double shFalse1 = (double)runMethod("Bank", local, "withdraw", new Object[]{"Name1", pin1, -20.25});
            String expected1 = "" + (50 - 10.50);
            String notExpected1 = "" + (50 - 10.50 + 20.25);

            double shTrue2 = (double)runMethod("Bank", local, "withdraw", new Object[]{"Name2", pin2, 10.50});
            double shTrue22 = (double)runMethod("Bank", local, "withdraw", new Object[]{"Name2", pin2, 50.25});
            String expected2 = "0.0";
            String notExpected2 = "" + (50 - 10.50 - 50.25);

            boolean shTrue3 = (boolean)runMethod("Bank", local, "deposit", new Object[]{"Name3", pin3, 10.25});
            boolean shFalse3 = (boolean)runMethod("Bank", local, "deposit", new Object[]{"Name3", pin3, -20.50});
            String expected3 = "" + (100 + 10.25);
            String notExpected3 = "" + (100 + 10.25 - 20.50);

            String a1 = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name1", pin1});
            String a2 = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name2", pin2});
            String a3 = (String)runMethod("Bank", local, "showAccount", new Object[]{"Name3", pin3});

            Object reval = runMethod("Bank", local, "deposit", new Object[]{"Name3", pin3-1, 10});
           boolean shFalse33 = true;
           Throwable throwme = null;
           if (reval instanceof Boolean)
               shFalse33 = (boolean)reval;
           else if (reval instanceof Throwable) {
                throwme = (Throwable)reval;
                throw throwme;
           }


            if (!(shTrue1>0 && shFalse1<=0
                && shTrue3 && !shFalse3 && !shFalse33)) {
                    depdraw.setFailStatus(1);
                    //depdraw.setPrintme("shTrue1: " + shTrue1 + ", shFalse1: " + shFalse1
                     //                   + ", shTrue3: " + shTrue3 + ", shFalse3: "
                     //                   + shFalse3 + ", shFalse33: " + shFalse33);
                   depdraw.setRationale("Values returned from the methods are incorrect.");
                    depdraw.setHelp(" Check that you handle null accounts correctly. Also make sure that, for deposit, successful transactions return true and unsucessful ones return false. For withdraw, successful transactions should return the amount withdrawn and unsuccessful should return a sentinel value that would never occur in a valid withdrawal.");
                    checks.add(depdraw);
                    closeJson();
                    return;
            }
            else if (!(shTrue1>0 && shFalse1<=0  && shTrue2>0 && shTrue22>0
                && shTrue3 && !shFalse3 && !shFalse33)) {
                    depdraw.setFailStatus(1);

                depdraw.setRationale("Withdraw return value incorrect");
                depdraw.setPrintme(
                        "Account 2: Start at 50\n\tWithdraw 10.50, which should return 10.5 and actually returns " + shTrue2 +
                        "\n\tWithdraw 50.25 (more than the balance), which should return 39.5 and actually returns " + shTrue22 + "\n\n"
                    );
                depdraw.setHelp(" For withdraw, successful transactions should return the amount withdrawn and unsuccessful should return a sentinel value that would never occur in a valid withdrawal.");
                    checks.add(depdraw);
                    closeJson();
                    return;
            }
            else if (!(a1.contains(expected1) && !a1.contains(notExpected1)
              && a2.contains(expected2) && !a2.contains(notExpected2)
              && a3.contains(expected3) && !a3.contains(notExpected3))) {
                    depdraw.setFailStatus(1);
                    depdraw.setRationale("Deposit or Withdraw logic incorrect");
                    depdraw.setPrintme(
                        "Account 1: Start at 50\n\tWithdraw 10.50\n\tThen try to withdraw a negative amount\nShould still be 39.50 and is:\n\t" + a1 + "\n\n" +
                        "Account 2: Start at 50\n\tWithdraw 10.50\n\tWithdraw more than the balance\nShould be 0.0 and is:\n\t" + a2 + "\n\n" +
                        "Account 3: Start at 100\n\tDeposit 10.25\n\tTry to withdraw a negative amount\nShould be 110.25 and is:\n\t" + a3 + "\n\n"
                    );
                    depdraw.setHelp("Look back at the deposit and withdraw methods in BankAccount and test their logic.");
                    checks.add(depdraw);
                    closeJson();
                    return;
                }
        } catch (Exception e) {
           depdraw.setFailStatus(1);
            depdraw.setRationale(getMsg(e));
            checks.add(depdraw);
            closeJson();
            return;
        } catch (Throwable e) {
           depdraw.setFailStatus(1);
            depdraw.setRationale(getMsg(e));
            checks.add(depdraw);
            closeJson();
            return;
        }
        depdraw.setRationale("Deposit and Withdraw logic looks correct");
        depdraw.setPass(true);
        checks.add(depdraw);

         // Check 14 - bankstring: Bank has a descriptive, user-friendly toString that includes the name, max number of accounts, and current number of accounts
               Check bankstring = new Check("bankstring", 1, 0);
        try {
            String badMethods = checkMethods("Bank", new String[]{"toString"});
            if (badMethods.length() > 0) {
                bankstring.setRationale("Your " + "Bank" + " class is missing these methods: " + badMethods.substring(0, badMethods.length()-2));
                bankstring.setHelp("Add the listed methods to your class; ensure their names are spelled correctly.");
                checks.add(bankstring);
                closeJson();
                return;
            }
        } catch (Exception e) {
            bankstring.setRationale(getMsg(e));
            bankstring.setHelp("Make sure you have all the methods for Bank as detailed in instructions");
            checks.add(bankstring);
            closeJson();
            return;
        }
         bankstring.setFailStatus(0);


       try {
        bankstring.setPrintme("Display toString with Bank Name");
        bankstring.setHelp("Make sure the toString method in Bank print's the Banks name, number of accounts currently there, and total number it can hold.");
                    Class localClass = Class.forName("Bank");
            Class[] parameterType = new Class[1];
            parameterType[0] = String.class;
            Bank local = (Bank)localClass.getDeclaredConstructor(parameterType).newInstance("Reading Coop");

            int pin3 = (Integer)runMethod("Bank", local, "addAccount", new Object[]{"Name3", 59.99});
            String bankStr = (String)runMethod("Bank", local, "toString", null);

            if (!(bankStr.contains("Reading Coop") && bankStr.contains("3") && bankStr.contains("1"))) {
                    bankstring.setRationale("Bank's toString doesn't contain all the expected info");
                    bankstring.setHelp("Make sure the toString for Bank returns the Bank name, number of accounts open, and total number of accounts it can have.");
                    checks.add(bankstring);
                    closeJson();
                    return;
                }
        } catch (Exception e) {
           bankstring.setFailStatus(1);
            bankstring.setRationale(getMsg(e));
            checks.add(bankstring);
            closeJson();
            return;
        }
        bankstring.setPass(true);
        checks.add(bankstring);


         // check 15 - check that BankClient is there and compiles and is longer than 13 lines
         // this happens in init

         // check 16 - Run it with an input to view an account and then quit (no runtime errors should happen)
         // this also happens in init?

        closeJson();
    }

    private static Field fieldIn(Field[] m, String name) {
        for (int i = 0; i < m.length; i++) {
            if (m[i].getName().equals(name))
                return m[i];
        }
        return null;
    }
    private static Method methodIn(Method[] m, String name) {
        for (int i = 0; i < m.length; i++) {
            if (m[i].getName().equals(name))
                return m[i];
        }
        return null;
    }

    public static String checkFields(String cla, String[] fields) {
        String fieldsNotWorking = "";
        try {
            Class c = Class.forName(cla);
            Field m[] = c.getDeclaredFields();
            for (String fie : fields) {
                Field field = fieldIn(m, fie);
                if (field==null) {
                    fieldsNotWorking += fie + ", ";
                }
            }
        }
        catch (Throwable e) {
            System.err.println(e);
            return e.toString();
        }
        return fieldsNotWorking;
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
            //System.out.println(method);
            if (method!=null) {
                Object res = method.invoke(c.cast(obj));
                return res;
            }
            else
                return null;
        }
        catch (Throwable e) {
            System.err.println(e);
            return e;
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

    public static String getMsg(Throwable e) {
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
      return msg.substring(0,msg.indexOf("Tester2.main")-5);
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
        expect += toString(this.expected[i]) + "\\n";
        act += toString(this.actual[i]) + "\\n";

      }
      String result = "{\"pass\": " + pass + ",\"actual\": \"" + act + "\",\"expected\": \"" + expect + "\",\"failStatus\": " + failStatus + ",\"checkId\": \"" + checkId + "\",\"help\": \"" + getHelp() + "\",\"printme\": \"" + getPrintme() + "\",\"rationale\": \"" + getRationale() + "\",\"visibility\": \"" + (true ? "visible" : "hidden" ) +  "\"}";
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

    public String getHelp() {return toString(help);}
    public void setHelp(String h) { help = h;}

    public String getPrintme() {return toString(printme);}
    public void setPrintme(String h) { printme = h;}

    public String getRationale() {return toString(rationale);}
    public void setRationale(String h) { rationale = h;}

        public static String toString(Object word) {
      return toString(word.toString());
   }
    public static String toString(String word) {
      if (word == null)
        return "";

      return word.replace("\\","\\\\").replace("\n", "\\n").replace("\r", "").replace("\f", "").replace("\t", "\\t").replace("\"","\\\"");
   }
}
