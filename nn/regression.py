import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import math
import csv


def load_csv(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader, None) # skip header
        for row in reader:
            data.append(row)
    return data


data = load_csv('../dataset/student-por.csv')

# Split dataset into testing and training set
random.shuffle(data)
test_size = len(data)/3
test_set = data[:test_size]
train_set = data[test_size:]

print "Testing Set:", len(test_set), "items"
print "Training Set:", len(train_set), "items"


# Sort test set by dependant variable to look nice on chart
test_set.sort(key=lambda x: int(x[-1]))
train_set.sort(key=lambda x: int(x[-1]))


# Separate inputs and outputs
x_test = [ x[:30] for x in test_set ]
y_test = [ [int(x[-1])] for x in test_set ]
x_train = [ x[:30] for x in train_set ]
y_train = [ [int(x[-1])] for x in train_set ]



def preprocess_row(row):
    row[0] = (row[0] == 'GP') # school
    row[1] = (row[1] == 'M') # sex
    row[2] = int(row[2]) # age
    row[3] = (row[3] == 'U') # address
    row[4] = (row[4] == 'GT3') # famsize
    row[5] = (row[5] == 'T') # Pstatus
    row[6] = int(row[6]) # Medu
    row[7] = int(row[7]) # Fedu
    jobs = ['teacher', 'health', 'services', 'at_home', 'other']
    row[8] = jobs.index(row[8]) # Mjob
    row[9] = jobs.index(row[9]) # Fjob
    reasons = ['home', 'reputation', 'course', 'other']
    row[10] = reasons.index(row[10]) # reason
    guardians = ['mother', 'father', 'other']
    row[11] = guardians.index(row[11]) # guardian
    row[12] = int(row[12]) # traveltime
    row[13] = int(row[13]) # studytime
    row[14] = int(row[14]) # failures
    row[15] = (row[15] == 'yes') # schoolsup
    row[16] = (row[16] == 'yes') # famsup
    row[17] = (row[17] == 'yes') # paid
    row[18] = (row[18] == 'yes') # activities
    row[19] = (row[19] == 'yes') # nursery
    row[20] = (row[20] == 'yes') # higher
    row[21] = (row[21] == 'yes') # internet
    row[22] = (row[22] == 'yes') # romantic
    row[23] = int(row[22]) # famrel
    row[24] = int(row[22]) # freetime
    row[25] = int(row[22]) # goout
    row[26] = int(row[22]) # Dalc
    row[27] = int(row[22]) # Walc
    row[28] = int(row[22]) # health
    row[29] = int(row[22]) # absences
    return row


# Preprocess dataset
x_test = [ preprocess_row(x) for x in x_test ]
x_train = [ preprocess_row(x) for x in x_train ]

#normalize(x_train, x_test)


# Parameters
learning_rate   = 0.001
training_epochs = 3000
display_step    = 100


# Network Parameters
n_hidden_1 = 15 # 1st layer num features
n_hidden_2 = 15 # 2nd layer num features
n_hidden_3 = 15 # 3nd layer num features
n_input = 30 # data input
n_output = 1


# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, 1])


# Create model
def multilayer_perceptron(_X, _weights, _biases):
    layer_1 = tf.nn.relu(tf.add(tf.matmul(_X, _weights['h1']), _biases['b1']))
    layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1, _weights['h2']), _biases['b2']))
    layer_3 = tf.nn.relu(tf.add(tf.matmul(layer_2, _weights['h3']), _biases['b3']))
    return tf.matmul(layer_3, _weights['out']) + _biases['out']


# Store layers weight & bias
stddev = 0.1 # <== This greatly affects accuracy!!
#mean = 1.0
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1],stddev=stddev)),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2],stddev=stddev)),
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3],stddev=stddev)),
    'out': tf.Variable(tf.random_normal([n_hidden_3, n_output],stddev=stddev))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_output]))
}


# Construct model
pred = multilayer_perceptron(x, weights, biases)


# Define loss and optimizer
cost = tf.reduce_mean(tf.square(pred - y))
#optm = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
optm = tf.train.AdamOptimizer(learning_rate).minimize(cost)
##corr = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
#accr = tf.reduce_mean(tf.cast(corr, "float"))


# Initializing the variables
init = tf.initialize_all_variables()


# Launch the graph
sess = tf.Session()
sess.run(init)


# Training cycle
training_costs = []
test_costs = []


for epoch in range(training_epochs):
    # Fit training
    #print(sess.run(pred, feed_dict={x: x_train, y: y_train}))
    sess.run(optm, feed_dict={x: x_train, y: y_train})
    # Compute average loss
    loss = sess.run(cost, feed_dict={x: x_train, y: y_train})
    test_loss = sess.run(cost, feed_dict={x: x_test, y: y_test})
    # Display logs per epoch step
    if epoch % display_step == 0:
        print ("Epoch: %03d/%03d train loss: %.9f test loss: %.9f" % (epoch, training_epochs, loss, test_loss))
        training_costs.append(loss)
        test_costs.append(test_loss)


train_loss = sess.run(cost, feed_dict={x: x_train, y: y_train})
test_loss = sess.run(cost, feed_dict={x: x_test, y: y_test})
print "Train Loss: ", train_loss
print "Test Loss: ", test_loss
print "Absolute Loss Difference: ", abs(test_loss - train_loss)



# Save plots

ys = sess.run(pred, feed_dict={x: x_train})

plt.plot(ys, 'bx', label='predicted grade')
plt.plot(y_train, 'rx', label='actual grade')
plt.legend(loc=4)

plt.ylabel('grade')
plt.xlabel('student #')
plt.savefig('accuracy_train.png', format='png')


plt.clf()

ys = sess.run(pred, feed_dict={x: x_test})

plt.plot(ys, 'bx', label='predicted grade')
plt.plot(y_test, 'rx', label='actual grade')
plt.legend(loc=4)

plt.ylabel('grade')
plt.xlabel('student #')
plt.savefig('accuracy_test.png', format='png')


plt.clf()

skip_steps = 1
plt.plot(range(display_step*skip_steps, training_epochs, display_step), training_costs[skip_steps:], label='training loss')
plt.plot(range(display_step*skip_steps, training_epochs, display_step), test_costs[skip_steps:], label='test loss')
plt.legend()
plt.ylabel('cost')
plt.xlabel('epoch')
plt.savefig('cost.png', format='png')


sess.close()
