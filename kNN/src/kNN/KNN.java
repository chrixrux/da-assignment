package kNN;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public  class KNN {
	public void classify (List<Instance> trainingSet, List<Instance> testSet, int k) {
		k = (k > trainingSet.size())? trainingSet.size(): k; 
		double sizeTestSet = testSet.size();
		double correctlyClassified = 0.0;
		double incorrectlyClassified = 0.0;
		
		//Store all possible class labels
		List<String> classLabels = new ArrayList<>();
		for (Instance instance: trainingSet) {
			if(!classLabels.contains(instance.classValue)) {
				classLabels.add(instance.classValue);
			}
		}
		Collections.sort(classLabels);
		
		int[][] confusionMatrix = new int[classLabels.size()][classLabels.size()];
		
		for(Instance instance: testSet) {
			List<Instance> neighbours = getKNearestNeighbours(trainingSet, instance, k);
			String predictedClassValue = getMostCommonClass(neighbours);
			
			
			//Get index of class label in map.  
			int predictedClassLabelIndex = classLabels.indexOf(predictedClassValue);
			int actualClassLabelIndex =  classLabels.indexOf(instance.classValue);
			
			confusionMatrix[predictedClassLabelIndex][actualClassLabelIndex]++;
			
			if(predictedClassValue.equals(instance.classValue)) {
				//System.out.println("Correctly classified! Prediction: " + predictedClassValue + " Class: " + instance.classValue);
				correctlyClassified++;
			} else {
				//System.out.println("Incorrectly classified! Prediction: " + predictedClassValue + " Class: " + instance.classValue);
				incorrectlyClassified++;
			}
		} 
		
		int[] numberOfInstancesPerClass = new int[classLabels.size()];
		int[] numberOfPredictionsPerClass = new int[classLabels.size()];
		int[] numberOfCorrectlyClassifiedInstancesPerClass = new int[classLabels.size()];
		
			for(int i = 0; i < classLabels.size(); i++) {
				numberOfCorrectlyClassifiedInstancesPerClass[i] = confusionMatrix[i][i];
				for(int j =0; j< classLabels.size(); j++) {
					numberOfInstancesPerClass[i] += confusionMatrix[j][i];
					numberOfPredictionsPerClass[i] += confusionMatrix[i][j];
			}
		}
			
		double[][] precisionAndRecall = new double[classLabels.size()][3];
		for(int i = 0; i < classLabels.size(); i++) {
			//Precision
			double precision = (double) numberOfCorrectlyClassifiedInstancesPerClass[i] /  (double) numberOfPredictionsPerClass[i]; 
			precisionAndRecall[i][0] = precision;
			//Recall
			double recall =  (double) numberOfCorrectlyClassifiedInstancesPerClass[i] / (double) numberOfInstancesPerClass[i];
			precisionAndRecall[i][1] = recall;
			//F1
			double f1 = 2 * precision * recall /(precision + recall);
			precisionAndRecall[i][2] = f1;
		}
		System.out.println("Classified using " + k + " nearest neighbours");
		System.out.println("Total test instances: " + sizeTestSet);
		System.out.println("Correctly classified instances: " + correctlyClassified);
		System.out.println("Incorreclty classified instances: " + incorrectlyClassified);
		double accuracy = correctlyClassified / sizeTestSet;
		System.out.println("Accuracy: " + accuracy);
		
		//System.out.println("The predicted class labels are listed vertical, while the actual class labels are listed horizontal. \n");
		System.out.println("\nConfusion Matrix:");
		System.out.print("Actual Class: \t");
		for(int i =0; i < classLabels.size(); i++){
			System.out.print("\t" + classLabels.get(i));
		}
		
		System.out.println();
		for (int i = 0; i< classLabels.size(); i++) {
			System.out.print("Predicted Class: " + classLabels.get(i) + "\t");
			for (int j =0; j < classLabels.size(); j++) {
				System.out.print(confusionMatrix[i][j] + "\t");
			}
			System.out.println();
		} 
		System.out.println();
		
		System.out.println(Arrays.toString(numberOfInstancesPerClass));
		System.out.println(Arrays.toString(numberOfPredictionsPerClass));
		System.out.println(Arrays.toString(numberOfCorrectlyClassifiedInstancesPerClass));
		
		System.out.println("\nStats Matrix:");
		System.out.println("Class \t Precision \t Recall \t F1");
		for (int i = 0; i< classLabels.size(); i++) {
			System.out.print( classLabels.get(i) + "\t");
			for (int j =0; j < 3; j++) {
				System.out.format("%.3f\t", precisionAndRecall[i][j]);
			}
			System.out.println();
		} 
		System.out.println();
		
	}
	
	
	private List<Instance> getKNearestNeighbours(List<Instance> trainingSet, Instance testInstance, int k) {
		List<Instance> neighbours = new ArrayList<>();
		
		//For each instance in the trainingSet the distance to the testInstance is calculated.
		for (Instance instance: trainingSet) {
			instance.distance = calculateEuclidieanDistance(instance, testInstance);	
		}
		//Sort arraylist ascending by distance
		Collections.sort(trainingSet);
		
		//Return first k elements of sorted List as neigbours;
		for(int i =0; i<k; i++) {
			neighbours.add(trainingSet.get(i));
		}
		return neighbours;
	}
	
	private String getMostCommonClass(List<Instance> neighbours) {
		HashMap<String, Integer> classCount = new HashMap<>();
		for (Instance instance: neighbours) {
			//If the class already exists in the map, the count is incremented. Otherwise, it is added to the map
			if(classCount.containsKey(instance.classValue)) {
				classCount.put(instance.classValue, classCount.get(instance.classValue) + 1);
			} else {
				classCount.put(instance.classValue, 1);
			}
		}
		int highestCount = 0;
		String mostCommonClass = "Error counting most common class";
		for(Entry<String,Integer> entry: classCount.entrySet()) {
			if(highestCount < entry.getValue()) {
				highestCount = entry.getValue();
				mostCommonClass = entry.getKey();
			}
		}
		return mostCommonClass;
	}
	
	private double calculateEuclidieanDistance(Instance from, Instance to) {
		double distance = 0.0;
		for(int i = 0; i < from.attributes.length; i++) {
			distance += Math.pow(from.attributes[i] - to.attributes[i], 2);
		}
		return Math.sqrt(distance);
	}
	
	private void evalConfusionMatrix(int[][] confusionMatrix, List<String> classLabels) {
		//It is assumed that the index of a class is the same in the list and confusion matrix. 
		//Additionally, it is assumed the target classes are stored horizontally and the output vertically. 
		
		double[] correctlyClassifiedPerClass = new double[classLabels.size()]; //This is basically, the diagonal of the confusion matrix
		double[] instancesPerClass = new double[classLabels.size()]; //Sum of each column 
		double[] predictionsPerClass = new double[classLabels.size()]; //Sum of each row
		
		for(int i = 0; i < classLabels.size(); i++) {
			correctlyClassifiedPerClass[i] = confusionMatrix[i][i];
			for(int j =0; j< classLabels.size(); j++) {
				instancesPerClass[i] += confusionMatrix[j][i];
				predictionsPerClass[i] += confusionMatrix[i][j];
		}
	}
	}
}
