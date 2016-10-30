#!/usr/bin/env python

import sys
import random

sys.path.append('../dataset')
import utils


# Split dataset into testing and training set

data = utils.load_csv('../dataset/student-por.csv', delimiter=';')

random.shuffle(data)
test_size = len(data)/3
test_set = data[:test_size]
train_set = data[test_size:]

utils.save_csv('../dataset/student-por-test.csv', test_set, delimiter=';')
utils.save_csv('../dataset/student-por-train.csv', train_set, delimiter=';')
