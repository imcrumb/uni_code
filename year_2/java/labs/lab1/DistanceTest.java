/**
*Test class for Distance class
*@author: Ian Lynch 109402039
*/
public class DistanceTest {

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