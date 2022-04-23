using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      double num1;
      double num2;
      double num3;

      Console.Write("Enter first number > ");

      num1 = Convert.ToDouble(Console.ReadLine() );

      Console.Write("Enter the second number > ");

      num2 = Convert.ToDouble(Console.ReadLine() );

      Console.Write("Enter the third number > ");

      num3 = Convert.ToDouble(Console.ReadLine() );

      double avg = (num1 + num2 + num3) / 3;

      Console.WriteLine(avg);


      Console.ReadKey();
    }
    
  }

}
  
