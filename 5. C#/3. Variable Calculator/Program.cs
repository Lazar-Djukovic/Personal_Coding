using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      // variable type needs to be declared, int for whole and we can use float or double or bool
      double num01;
      double num02;

      Console.Write("Input a number > ");

      //The input is converted to integer(or double, to variable type)
      num01 = Convert.ToDouble(Console.ReadLine() );

      Console.Write("Input the second number > ");

      //Converts to double so we can do decimals
      num02 = Convert.ToDouble(Console.ReadLine() );

      double result = num01 * num02;

      Console.WriteLine("The result is: " + result);

      //wait before closing
      Console.ReadKey();
    }
    
  }

}
  
