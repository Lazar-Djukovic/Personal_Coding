using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.Write("How many numbers do you want: ");

      int count = Convert.ToInt32(Console.ReadLine());

      for (int i = 1; i <= count; i++)
      {
        //2^i, 2 4 8 16 32 64...

        double result = Math.Pow(2, i);

        Console.WriteLine(result);
      }

      //end
      Console.ReadKey();
    }
    
  }

}
  
