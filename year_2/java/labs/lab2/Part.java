/**
*Superclass Bike representing generalised bike object
*@author Ian Lynch (109402039)
*/

public class Part {

	private final String PART_NAME;

	public Part(final String PART_NAME) {
		this.PART_NAME = PART_NAME;
	}

	public String toString(){
		return PART_NAME;
	}
}