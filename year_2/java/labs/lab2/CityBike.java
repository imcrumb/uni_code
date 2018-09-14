/**
*Subclass CityBike of Bike superclass
*@author Ian Lynch (109402039)
*/
public class CityBike extends LitBike {

	private static Frame frame = new HighFrame();
	private static Carrier carrier = new Carrier();

	public CityBike(){
		super();
	}

	@Override
	public void printComponents(){
		super.printComponents();
		System.out.println(frame);
		System.out.println(carrier);
	}

}