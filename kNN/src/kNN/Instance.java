package kNN;

import java.util.Arrays;

/**
 * This class represents an instance in a dataset
 * All attributes of this instance have to be numeric, except for the class variable it can have any value
 * @author christian
 *
 */
public class Instance implements Comparable<Instance> {
	public double[] attributes;
	public String classValue;
	//Will be set when calculating nearest neighbour
	public double distance;
	
	public Instance(double[] attributes, String classValue) {
		super();
		this.attributes = attributes;
		this.classValue = classValue;
	}	
	
	public String toString() {
		String output = "Attributes: " + Arrays.toString(attributes) + "Class: " + classValue;
		return output;
		
	}

	@Override
	public int compareTo(Instance o) {
		if(this.distance < o.distance) {
			return -1;
		} else if (this.distance > o.distance) {
			return 1;
		} else {
			return 0;
		}
	}
}
