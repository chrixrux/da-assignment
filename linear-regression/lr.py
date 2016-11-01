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

def fs(record):
	return x[:35]
    selected = []
    selected.append(record[0]) # school
    selected.append(record[6]) # Medu
    selected.append(record[7]) # Fedu
    selected.append(record[11]) # reason_reputation
    selected.append(record[18]) # studytime
    selected.append(record[19]) # failures
    selected.append(record[25]) # higher
    selected.append(record[31]) # Dalc
    selected.append(record[34]) # absences
    #return selected

test_set = [numerize(record) for record in test_set]
train_set = [numerize(record) for record in train_set]


# Sort test set by dependant variable to look nice on chart
test_set.sort(key=lambda x: float(x[35]))


# Separate inputs and outputs
x_test = [ fs(x) for x in test_set ]
avg_test = [ x[35] for x in test_set ]

x_train = [ fs(x) for x in train_set ]
avg_train = [ x[35] for x in train_set ]

print('Predict AVG Grade')
regr = linear_model.LinearRegression()
regr.fit(x_train, avg_train)

pred_test = regr.predict(x_test)

mse = np.mean((pred_test - avg_test) ** 2)
mae = np.mean(np.abs(pred_test - avg_test))

avg_train_avg = np.mean(avg_train)
avg_error = np.mean(np.abs(avg_test - avg_train_avg))
rae = mae/avg_error

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mse)
print("Mean absolute error: %.2f" % mae)
#print("AVG error: %.2f" % avg_error)
print("Relative absolute error: %.4f %%" % (rae * 100))
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

