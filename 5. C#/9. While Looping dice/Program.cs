using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      Random numberGen = new Random();
      
      int roll = 0;
      int attempts = 0;

      Console.WriteLine("Please enter to roll a die");

      while(roll != 6){
        Console.ReadKey();
        
        //first number is inclusie, but se second one is exclusive
        roll = numberGen.Next(1,7);
        Console.WriteLine("You rolled: " + roll);
        attempts++;
      }
      
      Console.WriteLine("It took you "+ attempts+" attempts to roll a six.");

      //end
      Console.ReadKey();
    }
    
  }

}
  
