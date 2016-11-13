import csv
from sklearn import tree
from sklearn.metrics import confusion_matrix

def load_csv(filename):
    # Read data from csv file
    data = []
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None) # skip header
        for row in reader:
            data.append(row)
    return data

def predict(y_train, y_test):
    # Create and train classifier
    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    # Make list of predicted values
    predicted = list(clf.predict(x_test))

    # Count and print number and percentage of correctly predicted values
    num_vals = len(predicted)
    correct = 0
    wrong = 0
    print("Total values: " + str(num_vals))
    for i in range(num_vals):
        if (int(predicted[i]) == int(y_test[i])):
            correct += 1
        else:
            wrong += 1
    print('Correct: ' + str(correct))
    print('Wrong: ' + str(wrong))
    print('Percent: ' + str(float(correct) / float(num_vals)))

    # Print confusion matrix
    print('Confusion matrix:')
    print(confusion_matrix(y_test, predicted))


# Load data
train_set = load_csv('../dataset/student-por-train-preprocessed-normalized.csv')
test_set = load_csv('../dataset/student-por-test-preprocessed-normalized.csv')

# Sort test set by dependant variable to look nice on chart
test_set.sort(key=lambda x: float(x[35]))

# Separate inputs and outputs
x_test = [ x[:35] for x in test_set ]
x_train = [ x[:35] for x in train_set ]
y_test_5level = [ x[36] for x in test_set ]
y_train_5level = [ x[36] for x in train_set ]
y_test_binary = [ x[37] for x in test_set ]
y_train_binary = [ x[37] for x in train_set ]


# Perform 5-level classification
print("5 level classification:")
predict(y_train_5level, y_test_5level)

# Perform binary classification
print("\nBinary classification:")
predict(y_train_binary, y_test_binary)