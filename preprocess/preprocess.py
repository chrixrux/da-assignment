#!/usr/bin/env python

import sys
import csv

sys.path.append('../dataset')
import utils

def filter_row(x):
	return int(x[32]) > 0

def grade_class(grade):
	if (grade >= 16):
		return 1
	elif (grade >= 14):
		return 2
	elif (grade >= 12):
		return 3
	elif (grade >= 10):
		return 4
	else:
		return 5

def calculate_avg_grade(data):
	sum = 0.

	for record in data:
		sum += record[35]

	return sum/len(data)

def append_grade_above_avg(row, avg_grade):
	row.append(int(row[35] > avg_grade))
	return row

def preprocess_row(x):
	grade_avg = round((int(x[30]) + int(x[31]) + int(x[32])) / 3., 1)
	grade_improvement = int(x[32]) - int(x[30])
	y = [
		int(x[0] == 'GP'), # school
		int(x[1] == 'M'), # sex
		int(x[2]), # age
		int(x[3] == 'U'), # address
		int(x[4] == 'GT3'), # famsize
		int(x[5] == 'T'), # Pstatus
		int(x[6]), # Medu
		int(x[7]), # Fedu
		# jobs = ['teacher', 'health', 'services', 'at_home', 'other']
		int(x[8] != 'at_home'), # Mjob
		int(x[9] != 'at_home'), # Fjob
		# reasons = ['home', 'reputation', 'course', 'other']
		int(x[10] == 'home'), # reason_home
		int(x[10] == 'reputation'), # reason_reputation
		int(x[10] == 'course'), # reason_course
		int(x[10] == 'other'), # reason_other
		# guardians = ['mother', 'father', 'other']
		int(x[11] == 'mother'), # guardian_mother
		int(x[11] == 'father'), # guardian_father
		int(x[11] == 'other'), # guardian_other
		int(x[12]), # traveltime
		int(x[13]), # studytime
		int(x[14]), # failures
		int(x[15] == 'yes'), # schoolsup
		int(x[16] == 'yes'), # famsup
		int(x[17] == 'yes'), # paid
		int(x[18] == 'yes'), # activities
		int(x[19] == 'yes'), # nursery
		int(x[20] == 'yes'), # higher
		int(x[21] == 'yes'), # internet
		int(x[22] == 'yes'), # romantic
		int(x[23]), # famrel
		int(x[24]), # freetime
		int(x[25]), # goout
		int(x[26]), # Dalc
		int(x[27]), # Walc
		int(x[28]), # health
		int(x[29]), # absences
		grade_avg, # grade_avg
		grade_class(grade_avg) # grade_avg_class
	]
	return y

def normalize_row(x):
	ndigits = 4
	# Min-max normalization: [0, 5] -> [0, 1]
	x[6] = round(float(x[6]) / 5, ndigits) # Medu
	x[7] = round(float(x[7]) / 5, ndigits) # Fedu
	# Min-max normalization: [1, 4] -> [0, 1]
	x[17] = round(float(x[17] - 1) / (4 - 1), ndigits) # traveltime
	x[18] = round(float(x[18] - 1) / (4 - 1), ndigits) # studytime
	# Min-max normalization: [0, 4] -> [0, 1]
	x[19] = round(float(x[19] - 0) / (4 - 0), ndigits) # failures
	# Min-max normalization: [1, 5] -> [0, 1]
	x[28] = round(float(x[28] - 1) / (5 - 1), ndigits) # famrel
	x[29] = round(float(x[29] - 1) / (5 - 1), ndigits) # freetime
	x[30] = round(float(x[30] - 1) / (5 - 1), ndigits) # goout
	x[31] = round(float(x[31] - 1) / (5 - 1), ndigits) # Dalc
	x[32] = round(float(x[32] - 1) / (5 - 1), ndigits) # Walc
	x[33] = round(float(x[33] - 1) / (5 - 1), ndigits) # health
	# Min-max normalization: [0, 93] -> [0, 1]
	x[34] = round(float(x[34]) / 93, ndigits) # absences
	return x

def main():
	if (len(sys.argv) != 3 and len(sys.argv) != 4 and (len(sys.argv) != 4 or sys.argv[3] != '--normalize')):
		print("usage: ./preprocess.py <input_file> <output_file> [--normalize]")
		print("./preprocess.py ../dataset/student-por-test.csv ../dataset/student-por-test-preprocessed-normalized.csv --normalize")
		print("./preprocess.py ../dataset/student-por-train.csv ../dataset/student-por-train-preprocessed-normalized.csv --normalize")
		exit()

	in_file = sys.argv[1]
	out_file = sys.argv[2]
	normalize = (len(sys.argv) == 4 and sys.argv[3] == '--normalize');

	data = utils.load_csv(in_file, ';')
	data = [ preprocess_row(row) for row in data if filter_row(row) ]

	avg_grade = calculate_avg_grade(data)
	data = [ append_grade_above_avg(row, avg_grade) for row in data ]

	if (normalize):
		data = [ normalize_row(row) for row in data ]

	header = [
		'school',
		'sex',
		'age',
		'address',
		'famsize',
		'Pstatus',
		'Medu',
		'Fedu',
		'Mjob',
		'Fjob',
		'reason_home',
		'reason_reputation',
		'reason_course',
		'reason_other',
		'guardian_mother',
		'guardian_father',
		'guardian_other',
		'traveltime',
		'studytime',
		'failures',
		'schoolsup',
		'famsup',
		'paid',
		'activities',
		'nursery',
		'higher',
		'internet',
		'romantic',
		'famrel',
		'freetime',
		'goout',
		'Dalc',
		'Walc',
		'health',
		'absences',
		'grade_avg',
		'grade_avg_class',
		'grade_above_avg'
	]
	data.insert(0, header);

	utils.save_csv(out_file, data, ',')

if __name__ == "__main__":
	main()
