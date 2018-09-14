/**
*Subclass LitBike inheriting from Bike superclass
*@author Ian Lynch (109402039)
*/
public class LitBike extends Bike {

	private static Light frontLight = new FrontLight();
	private static Light rearLight = new RearLight();

	public LitBike(){
		super();
	}

	@Override
	public void printComponents(){
		super.printComponents();
		System.out.println(frontLight);
		System.out.println(rearLight);
	}

}