import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
content=[]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        content.append(row)
print(content)