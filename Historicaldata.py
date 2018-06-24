import csv

with open('EUR_USD_Historical_Data.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	
	for line in csv_reader:
		print(line)
