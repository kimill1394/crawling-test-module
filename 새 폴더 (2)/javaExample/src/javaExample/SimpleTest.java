package javaExample;

public class SimpleTest {

	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
					
		
		
		Data d = new Data();
		d.x = 10;
		change(d.x);	// main이 static이니까 클래스 멤버 메서드만 불러다 쓸 수 있단닿ㅎㅎ
		System.out.println("After Change(): "+d.x);
		
		
	}
	
	
	static void change(int x) {
		x = 1000;
		
		System.out.println("change(): "+x);
	}

}



class Data {
	int x;
}