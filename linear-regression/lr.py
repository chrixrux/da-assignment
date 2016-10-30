from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report, r2_score
from sklearn import linear_model
import csv
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('../dataset')
import utils


test_set = utils.load_csv('../dataset/student-por-test-preprocessed-normalized.csv')
train_set = utils.load_csv('../dataset/student-por-train-preprocessed-normalized.csv')

def numerize(record):
    return [float(val) for val in record]

test_set = [numerize(record) for record in test_set]
train_set = [numerize(record) for record in train_set]


# Sort test set by dependant variable to look nice on chart
test_set.sort(key=lambda x: float(x[35]))


# Separate inputs and outputs
x_test = [ x[:35] for x in test_set ]
avg_test = [ x[35] for x in test_set ]

x_train = [ x[:35] for x in train_set ]
avg_train = [ x[35] for x in train_set ]

print('Predict AVG Grade')
regr = linear_model.LinearRegression()
regr.fit(x_train, avg_train)

pred_test = regr.predict(x_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((pred_test - avg_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_test, avg_test))


r2 = r2_score(avg_test, pred_test)
print('R2 Score (coefficient of determination): %f' % r2)

# Sort train set by dependant variable to look nice on chart
train_set.sort(key=lambda x_: float(x_[35]))
x_train = [ x_[:35] for x_ in train_set ]
avg_train = [ [float(x_[35])] for x_ in train_set ]

pred_train = regr.predict(x_train)

plt.plot(pred_train, 'bx', label='predicted grade')
plt.plot(avg_train, 'rx', label='actual grade')
plt.legend(loc=4)

plt.ylabel('grade')
plt.xlabel('student #')
plt.savefig('accuracy_train.png', format='png')


plt.clf()



plt.plot(pred_test, 'bx', label='predicted grade')
plt.plot(avg_test, 'rx', label='actual grade')
plt.legend(loc=4)

plt.ylabel('grade')
plt.xlabel('student #')
plt.savefig('accuracy_test.png', format='png')


plt.clf()

