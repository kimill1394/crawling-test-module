package mirae;

public class StarcraftUnit {

	
	static int idCounter = 0;
	int myId;
	
	
//	StarcraftUnit() {
//		
//		myId = ++idCounter;
//	
//	}

	
	
	void countid () {
		myId = ++idCounter;
	}
	
	
	
	public void printID() {
		System.out.println("ID is "+myId);
	}
	
}
