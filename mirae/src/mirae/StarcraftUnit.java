package mirae;

import mirae.ThisSuperExample;

public class StarcraftUnit {

	
	static int idCounter = 0;
	int myId;
	String name = "in StarUnit.java";
	
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
