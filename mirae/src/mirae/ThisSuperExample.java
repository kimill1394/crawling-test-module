package mirae;


/*	class StarcraftUnit {
		// ���� ��Ű���� �ٸ� Ŭ����, �̸��� ��ġ�� ��� ����
		// �̰� �����Ͽ����� 
		// �ֳĸ� public���� ���ǵ� �� �ֱ� ������ 
		// ��� �ڵ������� �� �ְ� �ڱ�� �̸��� ���ٴ� �� �˰� �ְŵ�!  
		String name = "in this .java";
}		// �ٸ� ��Ű���� ��쵵 �̸��� ���ٸ� import �� ���� Ǯ������ ��� ��!	
*/




// import package.class; 
// �������� �� �� �ְ� ���֣�������

public class ThisSuperExample {

	public static void main(String args[]) {
	
		computer cc = new computer();
		// ���� computer(������: Ŭ����)�� 
		// mirae.computer(Ǯ����: ��Ű��.Ŭ����)�� �����ϸ�
		
		
		
//		cc.printSuperOfSuperClassName();
		cc.printOverriding();
		
	}
	
}




class college {
   String name = "colleage name";
   
   
   college() {
	   super();
	   // �����ڰ����ؼ�, ���� Ŭ������ �����ڸ� ���� ���� ȣ���ؾ߸� �Ѵ�
	   // ��, �����ڸ� ȣ������ ������ ������ super() �� ȣ�����ִµ�
	   // ���� ���� Ŭ������ �⺻ �����ڰ� ���ٸ� ����! ��! ��!
	   // �ذ��1 ���� Ŭ������ �⺻ �����ڸ� ����ų� 
	   // �ذ��2 ���� Ŭ�������� ������ �Ű������� ���߰ų�
   }
   
   void printOverriding() {
	   System.out.println(this.name);
   }
}

class yeungjin extends college {
   String name = "yeungin";
   
   
   
   void printOverriding() {
	   super.printOverriding();
	   System.out.println(this.name);
   }
   
}

class computer extends yeungjin {
   String name = "computer";
   
   
   Object obj = super.getClass();
   
   void printSuperOfSuperClassName() {
      
      System.out.println(((college)this).name);
      // super�� ������ ����ȯ �� �� ���µ� 
      // this�� ���� ��ü�� ����Ű�� ���������� 
      // super�� ���� ��ü�� ���� ��ü�� ����Ű�� ������̱� ����
      
   }
   
   
   void printOverriding() {
	   super.printOverriding();
	   System.out.println(this.name);
	   // �������̵� ��� �� �߰�
	   // ���� �޼��带 �״�� ���� ��~�� �߰��ϰ� ���� �� superŰ���带 ����Ѵ�
	   
	   
	   // �������̵� �� �� ������ ��! 1
	   // �������̵� �ϴ� ��� �θ𺸴� ���������ڰ� ������ �� �ȴ�!
	   // �ֳĸ� �θ� �ȿ� �����σ����� �� �����غ�
	   
	   // �������̵� �� �� ������ ��! 2
	   // ������ ������ �� Ŀ�� �Դϴ�. ���߿� �������ش�褾.��
	   
   }
}
