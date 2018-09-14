public class Main {

	public static void main(String[] args){
		Bike bike = new Bike();
		System.out.println("Bike components:");
		bike.printComponents();

		MountainBike mountainBike = new MountainBike();
		System.out.println("\nMountianBike components:");
		mountainBike.printComponents();

		Hybrid hybrid = new Hybrid();
		System.out.println("\nHybrid components:");
		hybrid.printComponents();

		CityBike cityBike = new CityBike();
		System.out.println("\nCityBike components:");
		cityBike.printComponents();
	}

}