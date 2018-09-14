/**
*Hippo class
*@author Ian Lynch (109402039)
*/

public class Hippo implements Animal {

	public final Animal concreteHippo;


	public Hippo(){
		this.concreteHippo = new ConcreteHippo("Hippo.gif",true,10);
	}

	@Override
	public void eat(){
		concreteHippo.eat();
	}

	@Override
	public String food(){
		return concreteHippo.food();
	}

	@Override
	public void makeNoise(){
		concreteHippo.makeNoise();
	}

	@Override
	public void roam(){
		concreteHippo.roam();
	}
}
