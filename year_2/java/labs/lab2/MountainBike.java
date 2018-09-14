/**
*Subclass MountainBike inheriting from Bike superclass
*@author Ian Lynch (109402039)
*/
public class MountainBike extends Bike {

	private static Frame frame = new LowFrame();

	public MountainBike(){
		super();
	}

	@Override
	public void printComponents(){
		super.printComponents();
		System.out.println(frame);
	}

}