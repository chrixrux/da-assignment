from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import csv
import random
import sys

sys.path.append('../dataset')
import utils


test_set = utils.load_csv('../dataset/student-por-test-preprocessed-normalized.csv')
train_set = utils.load_csv('../dataset/student-por-train-preprocessed-normalized.csv')

def numerize(record):
    return [float(val) for val in record]

test_set = [numerize(record) for record in test_set]
train_set = [numerize(record) for record in train_set]


# Separate inputs and outputs
x_test = [ x[:35] for x in test_set ]
avg_test = [ x[37] for x in test_set ]
improvement_test = [ x[38] for x in test_set ]

x_train = [ x[:35] for x in train_set ]
avg_train = [ x[37] for x in train_set ]
improvement_train = [ x[38] for x in train_set ]

print('Predict AVG Grade Class')
gnb = GaussianNB()
avg_pred = gnb.fit(x_train, avg_train).predict(x_test)


print('Confusion Matrix')
matrix = confusion_matrix(avg_test, avg_pred)
print(matrix)

print('Classification Report')
report = classification_report(avg_test, avg_pred)
print(report)

# Predict Improvement
print('Predict Improvement Class')

gnb = GaussianNB()
improvement_pred = gnb.fit(x_train, improvement_train).predict(x_test)

print('Confusion Matrix')
matrix = confusion_matrix(improvement_test, improvement_pred)
print(matrix)

print('Classification Report')
report = classification_report(improvement_test, improvement_pred)
print(report)
