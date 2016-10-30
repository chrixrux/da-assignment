import csv

def load_csv(filename, delimiter=','):
	data = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=delimiter)
		next(reader, None) # skip header
		for row in reader:
			data.append(row)
	return data

def save_csv(filename, data, delimiter=','):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=delimiter)
		writer.writerows(data)
