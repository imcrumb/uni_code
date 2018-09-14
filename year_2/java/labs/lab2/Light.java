/**
*Subclass Light of superclass Part 
*@author Ian Lynch (109402039)
*/

public class Light extends Part {

	private final static String partName = "light";

	public Light(String lightType){
		super(lightType + partName);
	}

}