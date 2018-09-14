/**
*ConcreteCat class
*@author Ian Lynch (109402039)
*/

public class ConcreteCat implements Feline {

	public final String picture;
	public final boolean eatsGrass;
	public final int hungerLevel;

	public ConcreteCat(final String picture,
				final boolean eatsGrass,
				final int hungerLevel){
		this.picture = picture;
		this.eatsGrass = eatsGrass;
		this.hungerLevel = hungerLevel;
	}

	@Override
	public void eat(){
		System.out.println("Eating " + hungerLevel + " portions of " + food());
	}

	@Override
	public String food(){
		return (eatsGrass ? "grass":"meat");
	}

	@Override
	public void makeNoise(){
		System.out.println("Meow, meow");
	}

	@Override
	public void roam(){
		System.out.println("Cats roam solo..");
	}
}