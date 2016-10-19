#!/usr/bin/env python

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import math
import csv


def load_csv(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None) # skip header
        for row in reader:
            data.append(row)
    return data


data = load_csv('../dataset/student-por-preprocessed-normalized.csv')

# Split dataset into testing and training set
random.shuffle(data)
test_size = len(data)/3
test_set = data[:test_size]
train_set = data[test_size:]

print "Testing Set:", len(test_set), "items"
print "Training Set:", len(train_set), "items"


# Sort test set by dependant variable to look nice on chart
test_set.sort(key=lambda x: float(x[35]))


# Separate inputs and outputs
x_test = [ x[:35] for x in test_set ]
y_test = [ [float(x[35])] for x in test_set ]
x_train = [ x[:35] for x in train_set ]
y_train = [ [float(x[35])] for x in train_set ]


# Preprocess dataset
#x_test = [ preprocess_row(x) for x in x_test ]
#x_train = [ preprocess_row(x) for x in x_train ]

#normalize(x_train, x_test)


# Parameters
learning_rate   = 0.001
training_epochs = 2000
display_step    = 100


# Network Parameters
n_hidden_1 = 15 # 1st layer num features
n_hidden_2 = 15 # 2nd layer num features
n_hidden_3 = 15 # 3nd layer num features
n_input = 35 # data input
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

# Define stats
mae = tf.reduce_mean(tf.abs(pred - y))
mse = tf.reduce_mean(tf.square(pred - y))
rmse = tf.sqrt(mse)

y_avg = np.mean(y_train)
rae = mae/tf.reduce_mean(tf.abs(y_avg - y))
rrse = tf.sqrt(mse/tf.reduce_mean(tf.square(y_avg - y)))


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
    sess.run(optm, feed_dict={x: x_train, y: y_train})
    # Compute average loss
    loss = sess.run(cost, feed_dict={x: x_train, y: y_train})
    test_loss = sess.run(cost, feed_dict={x: x_test, y: y_test})
    # Display logs per epoch step
    if epoch % display_step == 0:
        print ("Epoch: %03d/%03d train loss: %.9f test loss: %.9f" % (epoch, training_epochs, loss, test_loss))
        training_costs.append(loss)
        test_costs.append(test_loss)


def get_stats(xs, ys):
    stats = {
        'loss': sess.run(cost, feed_dict={x: xs, y: ys}),
        'mae': sess.run(mae, feed_dict={x: xs, y: ys}),
        'rmse': sess.run(rmse, feed_dict={x: xs, y: ys}),
        'rae': sess.run(rae, feed_dict={x: xs, y: ys}),
        'rrse': sess.run(rrse, feed_dict={x: xs, y: ys})
    }
    return stats

def print_stats(stats):
    print "Loss (Mean Squared Error): ", round(stats['loss'], 4)
    print "Mean Absolute Error: ", round(stats['mae'], 4)
    print "Root Mean Squared Error: ", round(stats['rmse'], 4)
    print "Relative Absolute Error: ", round(stats['rae'] * 100, 4), '%'
    print "Root Relative Squared Error: ", round(stats['rrse'] * 100, 4), '%'

train_stats = get_stats(x_train, y_train)
test_stats = get_stats(x_test, y_test)

training_costs.append(train_stats['loss'])
test_costs.append(test_stats['loss'])


print "=== Train Set ==="
print_stats(train_stats)
print "=== Test Set ==="
print_stats(test_stats)
print "==="
print "Absolute Loss Difference: ", round(abs(test_stats['loss'] - train_stats['loss']), 4)


# Sort train set by dependant variable to look nice on chart
train_set.sort(key=lambda x_: float(x_[35]))
x_train = [ x_[:35] for x_ in train_set ]
y_train = [ [float(x_[35])] for x_ in train_set ]



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


plt.plot(range(display_step, training_epochs + display_step, display_step), training_costs[1:], label='training loss')
plt.plot(range(display_step, training_epochs + display_step, display_step), test_costs[1:], label='test loss')
plt.legend()
plt.ylabel('cost')
plt.xlabel('epoch')
plt.savefig('cost.png', format='png')


sess.close()
