import csv

file = open(f'C:\\Program Files\\Splunk\\etc\\apps\\sample_app\\bin\\sample_data.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)


rows = []
for row in csvreader:
    print(row[0],";", row[1],";",row[2])

file.close()

