import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')
outputpath = os.path.join('analysis', 'output.txt')
content=[]
voteDict = {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        content.append(row)

for row in content:
    candidate=row[2]
    if candidate in voteDict:
        voteDict={candidate:voteDict[candidate]+1}
    else:
        voteDict={candidate:1}
print(voteDict)