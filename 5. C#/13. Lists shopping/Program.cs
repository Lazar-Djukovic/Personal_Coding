using System;
using System.Collections.Generic;

namespace Hello
{
  class Program
  {
    static void Main(string[] args)
    {
      List<string> shoppingList = new List<string>();

      shoppingList.Add("Water");
      shoppingList.Add("Cheese");
      shoppingList.Add("Stuff");

      for (int i = 0; i < shoppingList.Count; i ++)
      {
        Console.WriteLine(shoppingList[i]);
      }
      
      shoppingList.Remove("Stuff");
      shoppingList.RemoveAt(1);

      Console.WriteLine("-----------------------");
      
      for (int i = 0; i < shoppingList.Count; i ++)
      {
        Console.WriteLine(shoppingList[i]);
      }

      
      Console.ReadKey();
    }
    
  }

}
  
