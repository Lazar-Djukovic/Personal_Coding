//A method that can count a number of words in a sentence.
using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      string input;
      int answer;
      Console.WriteLine("Please enter a sentence: ");
      input = Console.ReadLine();
      answer = Count(input);
      Console.WriteLine("Your sentence has " + answer + " words");  

      Console.ReadKey();
    }
    
    static int Count(string sentence)
    {

      string[] number = sentence.Split(' ');
      return number.Length;
    }
  }

}
  
