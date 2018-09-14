/**
*Superclass Bike representing generalised bike object
*@author Ian Lynch (109402039)
*/

public class Bike {

	private static Brakes brakes;
	private static Saddle saddle;
	private static Wheels wheels;
	private static Handlebar handlebar;


	public Bike(){
		brakes = new Brakes();
		saddle = new Saddle();
		wheels = new Wheels();
		handlebar = new Handlebar();
	}

	public void printComponents() {

		System.out.println(brakes);
		System.out.println(saddle);
		System.out.println(wheels);
		System.out.println(handlebar);

	}

}