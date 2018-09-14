/**
*Distance class takes distance in metres as parameter and converts distance to inches and feet
*@author: Ian Lynch 109402039
*/

public class Distance {

	private final double metreDistance;
	private static final double INCH_FACTOR = 39.37;
	private static final double FOOT_FACTOR = 3.28;

	public Distance(double distance) {
		metreDistance = distance;
	}

	public double getMetres() {
		return metreDistance;
	}

	public double getInches() {
		return metreDistance*INCH_FACTOR;
	}

	public double getFeet() {
		return metreDistance*FOOT_FACTOR;
	}

	public void printMetres() {
		System.out.println("Metres: " + metreDistance);
	}

	public void printInches() {
		System.out.println("Inches: " + getInches());
	}

	public void printFeet() {
		System.out.println("Feet: " + getFeet());
	}

	public static void main(String[] args) {
	Distance testOne = new Distance(1.0);
	testOne.printMetres();
	testOne.printInches();
	testOne.printFeet();

	Distance testTwo = new Distance(0.0);
	testTwo.printMetres();
	testTwo.printInches();
	testTwo.printFeet();

	Distance testThree = new Distance(1.5);
	testThree.printMetres();
	testThree.printInches();
	testThree.printFeet();
	}


}