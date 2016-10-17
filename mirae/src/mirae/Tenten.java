package mirae;

public class Tenten {

	
	public static void main(String args[]) {
		
		StarcraftUnit sUnit = new StarcraftUnit();
	
		Terran sTerran = new Terran();
	
		SCV sSCV = new SCV();
		Marine sMarine = new Marine();
		
		sUnit.printID();
		sTerran.printID();
		sSCV.printID();
		sMarine.printID();
	}
	
}
