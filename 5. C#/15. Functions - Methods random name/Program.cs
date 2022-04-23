using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      MeetAlien();

      Console.WriteLine("-------------");
      
      MeetAlien();

      Console.ReadKey();
    }
    
    static void MeetAlien()
    {
      Random numberGen = new Random();

      string name = "X-" + numberGen.Next(10,9999);
      int age = numberGen.Next(10,500);

      Console.WriteLine("Me name" + name);
      Console.WriteLine("old like umm " + age);
      Console.WriteLine("I like to eat pancake");
    }

  }

}
  
