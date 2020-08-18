import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')
outputpath = os.path.join('analysis', 'output.txt')
content=[]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        content.append(row)
print(content[2])