/**
*Cat class
*@author Ian Lynch (109402039)
*/

public class Cat implements Feline {

	public final Feline concreteCat;

	public Cat(){
		this.concreteCat = new ConcreteCat("Cat.gif",false,2);
	}

	@Override
	public void eat(){
		concreteCat.eat();
	}

	@Override
	public String food(){
		return concreteCat.food();
	}

	@Override
	public void makeNoise(){
		concreteCat.makeNoise();
	}

	@Override
	public void roam(){
		concreteCat.roam();
	}
}