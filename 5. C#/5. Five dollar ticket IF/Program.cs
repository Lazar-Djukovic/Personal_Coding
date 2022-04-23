using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Welcome! Put cash thank");

      int cash = Convert.ToInt32(Console.ReadLine());

      if (cash < 5) 
      {
        Console.WriteLine("No money sori");
      }
      else if (cash == 5)
      {
        Console.WriteLine("Thank you for 5$");
      }
      else 
      {
        int change = cash - 5;
        Console.WriteLine("Thank you for 5$");
        Console.WriteLine("Keep the change of " + change + "$");
      }

      //Read key before closing
      Console.ReadKey();
    }
    
  }

}
  
