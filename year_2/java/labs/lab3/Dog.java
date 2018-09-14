/**
*Dog class
*@author Ian Lynch (109402039)
*/

public class Dog implements Canine {

	public final Canine concreteDog;

	public Dog(){
		this.concreteDog = new ConcreteDog("Dog.gif",false,3);
	}

	@Override
	public void eat(){
		concreteDog.eat();
	}

	@Override
	public String food(){
		return concreteDog.food();
	}

	@Override
	public void makeNoise(){
		concreteDog.makeNoise();
	}

	@Override
	public void roam(){
		concreteDog.roam();
	}
}