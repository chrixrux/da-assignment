#!/usr/bin/env python

import sys
import csv

def load_csv(filename):
	data = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		next(reader, None) # skip header
		for row in reader:
			data.append(row)
	return data

def save_csv(filename, data):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=';')
		writer.writerows(data)

def preprocess_row(x):
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
		round((int(x[30]) + int(x[31]) + int(x[32])) / 3., 1) # grade
	]
	return y

def main():
	if (len(sys.argv) != 3):
		print("usage: ./preprocess.py <input_file> <output_file>")
		exit()

	in_file = sys.argv[1]
	out_file = sys.argv[2]

	data = load_csv(in_file)
	data = [ preprocess_row(row) for row in data ]
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
		'grade'
	]
	data.insert(0, header);

	save_csv(out_file, data)

if __name__ == "__main__":
	main()
