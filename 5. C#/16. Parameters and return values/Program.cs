using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      int answer = Multiply(34,83);
      Console.WriteLine(answer);
      
      if (answer % 2 == 0) 
      {
        Console.WriteLine(answer + " is even");
      } else
      {
        Console.WriteLine(answer + " is uneven");
      }

      Console.ReadKey();
    }
    
    static int Multiply(int num01, int num02)
    {
      int result = num01 * num02;
      return result;
    }

  }

}
  
