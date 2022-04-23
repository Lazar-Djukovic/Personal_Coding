using System;

namespace Hello
{
  class thing
  {
    public string name;
    public int age;

    public void DoStuff()
    {
      if (age > 20)
      {
        Console.WriteLine(name + age);
        age = -1;
      }

    }
  }

  class Program
  {
    static void Main(string[] args)
    {
      thing person01 = new thing();
      person01.name = "Laz";
      person01.age = 23;

      person01.DoStuff();
      person01.DoStuff();
      person01.DoStuff();

      //wait
      Console.ReadKey();
    }
    
  }

}
  
