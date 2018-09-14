/**
*Subclass Hybrid inheriting from Bike superclass
*@author Ian Lynch (109402039)
*/
public class Hybrid extends LitBike {

	private static Frame frame = new MediumFrame();

	public Hybrid(){
		super();
	}

	@Override
	public void printComponents(){
		super.printComponents();
		System.out.println(frame);
	}

}