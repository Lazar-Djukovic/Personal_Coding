using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      Random numberGen = new Random();
      
      int roll1 = -1;
      int roll2 = 0;
      int attempts = 0;

      Console.WriteLine("Please enter to roll a die");
      Console.WriteLine("-----------");

      while(roll1 != roll2){
        Console.ReadKey();
        
        //first number is inclusie, but se second one is exclusive
        roll1 = numberGen.Next(1,7);
        roll2 = numberGen.Next(1,7);
        Console.WriteLine("Dice 1: " + roll1);
        Console.WriteLine("Dice 2: " + roll2);
        Console.WriteLine("-----------");
        attempts++;
      }
      Console.WriteLine("You rolled the same number: " + roll1);
      Console.WriteLine("It took: " + attempts + " Attempts");
      //End
      Console.ReadKey();
    }
    
  }

}
  
