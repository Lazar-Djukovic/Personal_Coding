using System;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] stuff = {"Apple", "Pencil", "Table","Mug"};
      int len = stuff.Length;
      
      for (int i = 0; i < len; i++)
      {
        int rank = i+1;
        Console.WriteLine(rank + "."+ stuff[i] );
      }


      Console.ReadKey();
    }
    
  }

}
  
