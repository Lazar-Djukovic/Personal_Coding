using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("How many students are there? ");
      int snum = Convert.ToInt32(Console.ReadLine());
      string[] students = new string[snum];

      Console.WriteLine("Please input student names");
      Console.WriteLine("---------------");

      for (int i = 0; i < students.Length; i++) {
        students[i] = Console.ReadLine();
      }

      Console.WriteLine("here they are alphabetically: ");
      Console.WriteLine("---------------");

      Array.Sort(students);

      for (int i = 0; i < students.Length; i++)
      {
        Console.WriteLine(students[i]);
      }
      Console.ReadKey();
    }
    
  }

}
  
