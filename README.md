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

____

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

- **pathTo*Set:** Specifies the path to the dataset(s) relative to the current directory.
- **header:** Boolean variable specifying whether the dataset contains a header row with attribute names. If you use the program with a separate testing set, this value is applied to both sets.
- **percentage:** Percentage of the whole dataset to use for testing.
- **k:** Number of neighbors used for classification.
- **seed:** The seed used to select the test set. This is not necessary when using a separate test set.

**The last column of the set will always be chosen as the class label.**

#### How to reproduce the results
To reproduce the results that were discussed in the report in section 4.1 please make sure to use the provided datasets. Additionally, I assume you are in the kNN folder. Each example is presented in the form of the desired **goal**, the necessary **command** to achieve the goal, and the expected **output**.

**Goal:** Binary classify the provided test set (As in section 4.1.1 of the report).
**Command:**
```
java -jar kNN.jar ../dataset/kNN/kNN-binary-train.csv ../dataset/kNN/kNN-binary-test.csv true 1
```
**Output:**
```
Classified using 1 nearest neighbours
Total test instances: 210.0
Correctly classified instances: 129.0
Incorreclty classified instances: 81.0
Accuracy: 0.6142857142857143

Confusion Matrix:
Actual Class: 		1 	0
Predicted Class: 1	70	58
Predicted Class: 0	23	59
```
____

**Goal:** Perform multilevel classification with 5 class labels (As in section 4.1.2 of the report).
**Command:**
```
java -jar kNN.jar ../dataset/kNN/kNN-multilevel-train.csv ../dataset/kNN/kNN-multilevel-test.csv true 1

```
**Output:**
```
Classified using 1 nearest neighbours
Total test instances: 210.0
Correctly classified instances: 69.0
Incorreclty classified instances: 141.0
Accuracy: 0.32857142857142857

Confusion Matrix:
Actual Class: 	  1  2  3  4  5
Predicted Class: 1  5  3  5  5  3
Predicted Class: 2  4  6  14 13 7
Predicted Class: 3  4  6  23 22 8
Predicted Class: 4  2  5  8  18 11
Predicted Class: 5  1  2  5  13 17
```
**Comment:** 1 corresponds to "Very Good", ..., 5 corresponds to "Fail".
_____
