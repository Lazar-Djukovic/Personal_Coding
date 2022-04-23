using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      int ans1;
      int ans2;
      int ans3;

      Console.WriteLine("Whats 16x3 + 9?");
      ans1 = Convert.ToInt32(Console.ReadLine());
      if(ans1 == 57) {
        Console.WriteLine("Correct");
      } 
      
      else {
        Console.WriteLine("Wrong answer, the correct answer was 57");

      }
      Console.WriteLine("Whats 2+2x5+6?");
      ans2 = Convert.ToInt32(Console.ReadLine());
      if(ans2 == 18) {
        Console.WriteLine("Correct");
       
      } 

      else {
        Console.WriteLine("Wrong answer, the correct answer was 18");
 
      }

     Console.WriteLine("Whats 25-14+6x2?");
      ans3 = Convert.ToInt32(Console.ReadLine());
      if(ans3 == 23) {
        Console.WriteLine("Correct");
        
      } 
      else {
        Console.WriteLine("Wrong answer, the correct answer was 57");
      }

      //wait
      Console.ReadKey();
    }
    
  }

}
  
