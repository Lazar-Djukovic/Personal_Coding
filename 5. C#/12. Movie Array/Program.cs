using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] movies = new string[4];

      Console.WriteLine("Type 4 movies");
      Console.WriteLine("---------------");

      for (int i = 0; i < movies.Length; i++)
      {
        movies[i] = Console.ReadLine();
      }

      Console.WriteLine("here they are alphabetically: ");
      Console.WriteLine("---------------");

      Array.Sort(movies);

      for (int i = 0; i < movies.Length; i++)
      {
        Console.WriteLine(movies[i]);
      }

      Console.ReadKey();

    }
    
  }

}
  
//10.01 minute in video