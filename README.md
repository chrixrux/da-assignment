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
Actual Class: 		0	1
Predicted Class: 0	59	23
Predicted Class: 1	58	70

Evaluation Metrics:
Class 	 Precision 	 Recall 	 F1
0          0.720          0.504          0.593
1          0.547          0.753          0.633

Average Evaluation Metrics:
Precision: 0.633
Recall:    0.628
F1:        0.613
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
Actual Class: 		1	2	3	4	5
Predicted Class: 1	5	3	5	5	3
Predicted Class: 2	4	6	14	13	7
Predicted Class: 3	4	6	23	22	8
Predicted Class: 4	2	5	8	18	11
Predicted Class: 5	1	2	5	13	17

Evaluation Metrics:
Class 	 Precision 	 Recall 	 F1
1          0.238          0.313          0.270
2          0.136          0.273          0.182
3          0.365          0.418          0.390
4          0.409          0.254          0.313
5          0.447          0.370          0.405

Average Evaluation Metrics:
Precision: 0.319
Recall:    0.325
F1:        0.312
```
**Comment:** 1 corresponds to "Very Good", ..., 5 corresponds to "Fail".
_____


### Neural Network for Regression
Neural network is implemented in Python with use of TensorFlow library.

There is a train and test set loss printed every 100 training epochs on output. In the end, summary is printed separately for train and test set.

**Command:**
```
python regression.py
```

**Output:**
```
Testing Set: 210 items
Training Set: 422 items
Epoch: 000/4000 train loss: 92.057121277 test loss: 86.788223267
Epoch: 100/4000 train loss: 55.891376495 test loss: 51.652065277
Epoch: 200/4000 train loss: 16.942264557 test loss: 14.748498917
Epoch: 300/4000 train loss: 7.214027882 test loss: 6.719604492
Epoch: 400/4000 train loss: 6.745038509 test loss: 6.662531853
Epoch: 500/4000 train loss: 6.589032650 test loss: 6.574604511
Epoch: 600/4000 train loss: 6.435916424 test loss: 6.467381001
Epoch: 700/4000 train loss: 6.284482479 test loss: 6.362630844
Epoch: 800/4000 train loss: 6.135331631 test loss: 6.261366844
Epoch: 900/4000 train loss: 5.989159584 test loss: 6.164131641
Epoch: 1000/4000 train loss: 5.846632481 test loss: 6.071414471
Epoch: 1100/4000 train loss: 5.708371162 test loss: 5.983677387
Epoch: 1200/4000 train loss: 5.574954987 test loss: 5.901334763
Epoch: 1300/4000 train loss: 5.446936607 test loss: 5.824734211
Epoch: 1400/4000 train loss: 5.324831009 test loss: 5.754186630
Epoch: 1500/4000 train loss: 5.209113598 test loss: 5.689904690
Epoch: 1600/4000 train loss: 5.100202560 test loss: 5.632014751
Epoch: 1700/4000 train loss: 4.998434544 test loss: 5.580493927
Epoch: 1800/4000 train loss: 4.904023647 test loss: 5.535174370
Epoch: 1900/4000 train loss: 4.817032337 test loss: 5.495689869
Epoch: 2000/4000 train loss: 4.737352848 test loss: 5.461502075
Epoch: 2100/4000 train loss: 4.664692402 test loss: 5.431900501
Epoch: 2200/4000 train loss: 4.598586559 test loss: 5.406054020
Epoch: 2300/4000 train loss: 4.538440228 test loss: 5.383089542
Epoch: 2400/4000 train loss: 4.483576775 test loss: 5.362171650
Epoch: 2500/4000 train loss: 4.433307171 test loss: 5.342582703
Epoch: 2600/4000 train loss: 4.386981487 test loss: 5.323789120
Epoch: 2700/4000 train loss: 4.344039917 test loss: 5.305459499
Epoch: 2800/4000 train loss: 4.304032326 test loss: 5.287471294
Epoch: 2900/4000 train loss: 4.266623020 test loss: 5.269864559
Epoch: 3000/4000 train loss: 4.231579304 test loss: 5.252801895
Epoch: 3100/4000 train loss: 4.198749065 test loss: 5.236505985
Epoch: 3200/4000 train loss: 4.168040752 test loss: 5.221213341
Epoch: 3300/4000 train loss: 4.139398098 test loss: 5.207134724
Epoch: 3400/4000 train loss: 4.112786770 test loss: 5.194436073
Epoch: 3500/4000 train loss: 4.088179111 test loss: 5.183216572
Epoch: 3600/4000 train loss: 4.065546513 test loss: 5.173519611
Epoch: 3700/4000 train loss: 4.044847965 test loss: 5.165315628
Epoch: 3800/4000 train loss: 4.026030540 test loss: 5.158532619
Epoch: 3900/4000 train loss: 4.009027004 test loss: 5.153046608
=== Train Set ===
Loss (Mean Squared Error):  3.9939
Mean Absolute Error:  1.5929
Root Mean Squared Error:  1.9985
Relative Absolute Error:  74.8969 %
Root Relative Squared Error:  76.5661 %
=== Test Set ===
Loss (Mean Squared Error):  5.1487
Mean Absolute Error:  1.7946
Root Mean Squared Error:  2.2691
Relative Absolute Error:  87.6588 %
Root Relative Squared Error:  91.0855 %
===
Absolute Loss Difference:  1.1548
```
____


### Linear Regression
Linear regression is implemented in Python using scikit-learn package.

**Command:**
```
python lr.py
```

**Output:**
```
Predict AVG Grade
('Coefficients: \n', array([  6.23495532e-01,  -3.82159144e-01,   1.76563389e-01,
         6.43945456e-03,  -1.67556713e-01,   2.78285674e-01,
         2.15296300e+00,   6.07023945e-01,  -9.81721382e-02,
        -3.06865004e-03,   3.48227738e+13,   3.48227738e+13,
         3.48227738e+13,   3.48227738e+13,  -1.21717387e+13,
        -1.21717387e+13,  -1.21717387e+13,   1.69375603e-01,
         1.32861879e+00,  -4.51626664e+00,  -8.14978279e-01,
        -1.91027258e-01,  -9.14310711e-01,   3.20654298e-01,
        -1.92913455e-01,   1.45198424e+00,   3.06362941e-01,
        -4.10465501e-01,   1.67146812e-02,  -1.22052646e-01,
         2.98080402e-03,  -6.07930660e-01,  -6.38894714e-01,
        -2.50024437e-01,  -5.46703684e+00]))
Mean squared error: 5.07
Mean absolute error: 1.77
Relative absolute error: 86.6668 %
Variance score: 0.17
R2 Score (coefficient of determination): 0.174584
```
____


### Naive Bayes
Naive Bayes is implemented in Python using scikit-learn package.

**Command:**
```
python bayes.py
```

**Output:**
```
Predict AVG Grade Class
Confusion Matrix
[[15  0  1  0  0]
 [19  2  0  0  1]
 [49  2  0  3  1]
 [56  0  3  7  5]
 [21  0  0  8 17]]
Classification Report
             precision    recall  f1-score   support

        1.0       0.09      0.94      0.17        16
        2.0       0.50      0.09      0.15        22
        3.0       0.00      0.00      0.00        55
        4.0       0.39      0.10      0.16        71
        5.0       0.71      0.37      0.49        46

avg / total       0.35      0.20      0.19       210

Accuracy: 0.195238095238

Predict Above AVG
Confusion Matrix
[[58 59]
 [17 76]]
Classification Report
             precision    recall  f1-score   support

        0.0       0.77      0.50      0.60       117
        1.0       0.56      0.82      0.67        93

avg / total       0.68      0.64      0.63       210

Accuracy: 0.638095238095
```
____
