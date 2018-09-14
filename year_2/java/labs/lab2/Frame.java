/**
*Subclass Frame of superclass Part 
*@author Ian Lynch (109402039)
*/

public class Frame extends Part {

	private final static String partName = "frame";

	public Frame(String frameType){
		super(frameType + partName);
	}

}