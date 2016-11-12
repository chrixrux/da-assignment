from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import csv
import random
import sys

sys.path.append('../dataset')
import utils


test_set = utils.load_csv('../dataset/student-por-test-preprocessed-normalized.csv')
train_set = utils.load_csv('../dataset/student-por-train-preprocessed-normalized.csv')

def numerize(record):
    return [float(val) for val in record]

def fs(record):
    return x[:35]
    selected = []

test_set = [numerize(record) for record in test_set]
train_set = [numerize(record) for record in train_set]


# Separate inputs and outputs
x_test = [ fs(x) for x in test_set ]
avg_test = [ x[36] for x in test_set ]
above_test = [ x[37] for x in test_set ]

x_train = [ fs(x) for x in train_set ]
avg_train = [ x[36] for x in train_set ]
above_train = [ x[37] for x in train_set ]

print('Predict AVG Grade Class')
gnb = GaussianNB()
avg_pred = gnb.fit(x_train, avg_train).predict(x_test)


print('Confusion Matrix')
matrix = confusion_matrix(avg_test, avg_pred)
print(matrix)

print('Classification Report')
report = classification_report(avg_test, avg_pred)
print(report)

accuracy = accuracy_score(avg_test, avg_pred)
print('Accuracy: ' + str(accuracy))

# Predict Improvement
print('\nPredict Above AVG')

gnb = GaussianNB()
above_pred = gnb.fit(x_train, above_train).predict(x_test)

print('Confusion Matrix')
matrix = confusion_matrix(above_test, above_pred)
print(matrix)

print('Classification Report')
report = classification_report(above_test, above_pred)
print(report)

accuracy = accuracy_score(above_test, above_pred)
print('Accuracy: ' + str(accuracy))
