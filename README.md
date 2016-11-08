# NTU CZ4032 - Data Analytics and Mining - Group 34
## Predicting School Performance in Portuguese Youth
This is the plain README.txt file, however we recommend to read the formatted Markdown file available at: https://github.com/chrixrux/da-assignment.

### Group Members
Name | Matric. Number
---- | -------------
Skala Matous | N1602866H
Widmer Christian | N1602590C
Hunshamar Bjørnar | N1602951E
Efrem Afework Yared | N1603716J
Groschupp Friederike Juliane | N1602589L
Arcenas Carlos Alberto Lagdameo | N1604152E

### k nearest Neighbour  
The k nearest neighbor algorithm was implemented in Java from scratch. It can be used either with a training set and a separate test set or just one set with a specified percentage to use for testing.
Please make sure that only valid CSV files, i.e. commas as delimiters and dots as decimal separators, are passed as arguments.

The submitted zip contains all files necessary to build and run the algorithm. Please navigate to the kNN folder and type `ant` to execute the Ant build file and create the runnable jar. Afterwards you can type
```
java -jar kNN.jar pathToTrainingSet pathToTestSet header k
```
to run the program with two separate sets or type
```
java -jar kNN.jar pathToDataset header percentage k seed
```
to start it with just one set.

* **pathTo*Set:** Specifies the path to the dataset(s) relative to the current directory.
* **header:** Boolean variable specifying whether the dataset contains a header row with attribute names. If you use the program with a separate testing set, this value is applied to both sets.
* **percentage:** Percentage of the whole dataset to use for testing.
* **k:** Number of neighbors used for classification.
* **seed:** The seed used to select the test set. This is not necessary when using a separate test set.

**The last column of the set will always be chosen as the class label.**

To reproduce the results that were discussed in the report in section X.X.X  ... To be continued.
