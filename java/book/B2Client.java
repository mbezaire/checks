

public class B2Client
{
   public static void main(String[] args)
   {
      Book myBook = new Book("An Other World","Edward is Young",5.43);
      myBook.setTitle("An Immense World");
      myBook.getAuthor().setName("Ed Yong");
      myBook.setWholesale(85.43);
      System.out.println(myBook);
   }
}