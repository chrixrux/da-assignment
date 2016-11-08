package kNN;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/** 
 * This class is used to parse a csv file. It
 * @author christian
 *
 */
public class CSVParser {
	private static  String DELIMITER = ",";
	/**
	 * 
	 * @param path to the csv file
	 * @param header is true if the first row is a header row specifing the names of the attributes. false otherwise
	 */
	
	public static List<Instance> parseCSV(String path, boolean header) {
		List<Instance> instanceList = new ArrayList<>();
		
		try {
			FileReader csvFileReader = new FileReader(path);
			BufferedReader br = new BufferedReader(csvFileReader);
			String row = "";
			//Skip the first row if it is the header row
			if(header) {
				row = br.readLine();
			}
			
			while ((row = br.readLine()) != null) {
				String[] attributes = row.split(DELIMITER);
				double[] attr = new double[attributes.length-1];
				
				for (int i =0; i <= attributes.length - 2; i++) {
					try {
						attr[i] = Double.parseDouble(attributes[i]);		
					} catch (NumberFormatException ex) {
						System.out.println("All attributes except the last (the class) have to be numeric");
						
					}
				}
				
				String classValue = attributes[attributes.length-1];
				instanceList.add(new Instance(attr, classValue));
			}
			br.close();
		} catch (FileNotFoundException e) {
			System.out.println("File " + path + " could not be found" );
			System.exit(0);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return instanceList;
		
	}

}
