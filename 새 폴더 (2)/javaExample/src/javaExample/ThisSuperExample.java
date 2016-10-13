package javaExample;

public class ThisSuperExample {

	public static void main(String args[]) {
	
		computer cc = new computer();
		cc.printdoublesuperclassName();
		
	}
	
}




class college {
   String name = "colleage name";
}

class yeungjin extends college {
   String name = "yeungin";
}

class computer extends yeungjin {
   String name = "computer";
   
   
   Object obj = super.getClass();
   
   void printdoublesuperclassName() {
      
      System.out.println(((college)this).name);
   }
}