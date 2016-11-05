NTU CZ4032 - Data Analytics and Mining - Group 34
Predicting School Performance in Portuguese Youth
This is the plain README.txt file, however we recommend to read the formatted Markdown file available at: https://github.com/chrixrux/da-assignment.

Group Members
|Name                            | Matric. Number|
|--------------------------------|---------------|
|Skala Matous                    |
|Widmer Christian                | N1602590C     |
|Hunshamar Bjørnar               |
|Efrem Afework Yared             |
|Groschupp Friederike Juliane    | N1602589L     |
|Arcenas Carlos Alberto Lagdameo |

k nearest Neighbour
The k nearest neighbour algorithm was implemented in Java from scratch. It can be used either with a training set and a seperate test set or just one set with a specified percentage to use for testing.
Please make sure that only valid CSV files, i.e. commas as delimiters and dots as decimal seperators, are passed as arugments.

Please navigate to the kNN folder and type

java -jar kNN.jar pathToTrainingSet pathToTestSet header k

to run the program with two seperate sets or type

java -jar kNN.jar pathToDataset header percentage k seed

to start it with just one set.

* pathTo*Set: Specifies the path to the dataset(s) relative to the current directory.
* header: Boolean variable specifying whether the dataset contains a header row with attribute names. If you use the program with a separate testing set, this value is applied to both sets.
* percentage: Percentage of the whole dataset to use for testing.
* k: Number of neighbours used for classfication.
* seed: The seed used to select the test set. This is not necessary when using a sperate test set.

To reproduce the results that were discussed in the report in section X.X.X  ... To be continued.
