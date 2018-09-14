/**
*Main class
*@author Ian Lynch (109402039)
*/

public class Main {

	public static void main(String[] args){
		System.out.println("\nHIPPO");
		final Hippo hippo = new Hippo();
		hippo.eat();
		System.out.println("FOOD: " + hippo.food());
		hippo.makeNoise();
		hippo.roam();

		System.out.println("\nCAT");
		final Cat cat = new Cat();
		cat.eat();
		System.out.println("FOOD: " + cat.food());
		cat.makeNoise();
		cat.roam();

		System.out.println("\nDOG");
		final Dog dog = new Dog();
		dog.eat();
		System.out.println("FOOD: " + dog.food());
		dog.makeNoise();
		dog.roam();

	}

}