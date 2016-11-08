package kNN;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * The executable .jar file for the algorithm is provided with the report and
 * can be used in the terminal. There are two ways to use the algorithm either
 * with separate test and training sets or one full set and a specified
 * percentage to use for testing.
 * 
 * To use the program with a separate test set please type:
 * 
 * java -jar kNN.jar pathToTrainingSet pathToTestSet header k
 * 
 * 
 * To use the algorithm with one full set and a percentage for testing please
 * type:
 * 
 * java -jar kNN.jar path header percentage k seed
 
 * 
 * All parameters are required to run the program.
 * 
 * Path: The path to the dataset(s). Make sure it's a CSV file using commas as
 * separators and dots to seperate decimals. 
 * Header: Boolean variable specifying whether the dataset contains a header row with attribute names. If you use
 * the program with a separate testing set, this value is applied to both sets.
 * Percentage: Percentage of the whole dataset to use for testing.
 * k: Number of neighbours used for classfication. 
 * seed: The seed used to select the test set. This is not necessary when using a sperate test set.
 * 
 * @author christian
 *
 */
public class Main {
	static List<Instance> testList;
	static List<Instance> trainingList;
	static int k;
	public static void main(String[] args) {
	
	if(args.length == 5) {
		//one set with a test percentage
		String pathToSet = args[0];
		
		if(!pathToSet.contains(".csv")) {
			System.err.println("Please only provide CSV files.");
			System.exit(0);
		}
		
		boolean header = Boolean.parseBoolean(args[1]);
		
		try {
			double testPercentage = Double.parseDouble(args[2]);
			k = Integer.parseInt(args[3]);
			int seed = Integer.parseInt(args[4]);
			List<Instance> completeList = CSVParser.parseCSV(pathToSet, header);
			 testList = getTestList(testPercentage, completeList, seed);
			 trainingList = completeList;
			} catch (NumberFormatException e) {	
				System.err.println("Parameters 3 to 5 should be numeric");
				printUsage();
				System.exit(0);
			}
		
	} else if (args.length == 4) {
		// two separate sets for testing and training
		String pathToTrainigSet = args[0];
		String pathToTestSet = args[1];
		
		if(!(pathToTrainigSet.contains(".csv") && pathToTestSet.contains(".csv"))) {
			System.err.println("Please only provide CSV files.");
			printUsage();
			System.exit(0);
		}
		
		boolean header = Boolean.parseBoolean(args[2]);
		trainingList = CSVParser.parseCSV(pathToTrainigSet, header);
		testList = CSVParser.parseCSV(pathToTestSet, header);
		
		try{
			k = Integer.parseInt(args[3]);
		} catch (NumberFormatException ex) {
			System.err.println("K should be an integer");
			printUsage();
			System.exit(0);
		}
	} else {
		System.err.println("Wrong parameters specified");
		printUsage();
		System.exit(0);
	} 
	
	if(k <= 0) {
		System.err.println("k should be greater than 0");
		printUsage();
		System.exit(0);
	}
	
	KNN kNN = new KNN();
	kNN.classify(trainingList, testList, k);

}

	public static void printUsage() {
		System.out.println("To use the program with a separate test set please type: \n \n "
				+ "java -jar kNN.jar pathToTrainingSet pathToTestSet header k \n \n"
				+ " To use the algorithm with one full set and a percentage for testing please type: \n\n"
				+ " java -jar kNN.jar path header percentage k seed \n\n"
				+ "All parameters are required to run the program. \n"
				+ "Path: The path to the dataset(s). Make sure it's a CSV file using commas as separators and dots to seperate decimals.\n "
				+ "Header: Boolean variable specifying whether the dataset contains a header row with attribute names. \n"
				+ "If you use the program with a separate testing set, this value is applied to both sets. \n"
				+ "Percentage: Percentage of the whole dataset to use for testing.\n"
				+ " k: Number of neighbours used for classfication.\n "
				+ "seed: The seed used to select the test set. This is not necessary when using a sperate test set.");
	}

	public static List<Instance> getTestList(double percentage, List<Instance> completeList, int seed) {
		double numberOfTestInstances = percentage * completeList.size();
		List<Instance> testList = new ArrayList<>();
		Random random = new Random(seed);
		for (int i = 0; i < numberOfTestInstances; i++) {
			int index = random.nextInt(completeList.size());
			testList.add(completeList.remove(index));
		}
		return testList;
	}
}
