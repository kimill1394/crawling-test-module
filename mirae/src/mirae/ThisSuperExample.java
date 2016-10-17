package mirae;

public class ThisSuperExample {

	public static void main(String args[]) {
	
		computer cc = new computer();
//		cc.printSuperOfSuperClassName();
		cc.printOverriding();
		
	}
	
}




class college {
   String name = "colleage name";
   
   
   college() {
	   super();
	   // 생성자관련해서, 상위 클래스의 생성자를 가장 먼저 호출해야만 한다
	   // 단, 생성자를 호출하지 않으면 저절로 super() 를 호출해주는데
	   // 만약 상위 클래스에 기본 생성자가 없다면 에러! 발! 생!
	   // 해결법1 상위 클래스에 기본 생성자를 만들거나 
	   // 해결법2 하위 클래스에서 생성자 매개변수를 맞추거나
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
      // super는 저렇게 형변환 할 수 없는데 
      // this는 현재 객체를 가리키는 참조변수고 
      // super는 현재 객체의 상위 객체를 가리키는 예약어이기 때문
      
   }
   
   
   void printOverriding() {
	   super.printOverriding();
	   System.out.println(this.name);
	   // 오버라이딩 방법 중 추가
	   // 상위 메서드를 그대로 쓰고 조~금 추가하고 싶을 때 super키워드를 사용한다
	   
	   
	   // 오버라이딩 할 때 주의할 점! 1
	   // 오버라이딩 하는 경우 부모보다 접근제한자가 좁으면 안 된다!
	   // 왜냐면 부모가 안에 있으니깧ㅎㅎ 잘 생각해봐
	   
	   // 오버라이딩 할 때 주의할 점! 2
	   // 예외의 범위도 더 커야 함니당. 나중에 설명해준대욤ㅎ.ㅎ
	   
   }
}
