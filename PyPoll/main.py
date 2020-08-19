import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')
outputpath = os.path.join('analysis', 'output.txt')
content=[]
voteDict = {}
winner=None
total = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        content.append(row)

for row in content:
    candidate=row[2]
    total=total+1
    if candidate in voteDict:
        voteDict[candidate]=voteDict[candidate]+1
    else:
        voteDict[candidate]=1

results=[]
for candidate in voteDict:
    results.append(f"{candidate}: {voteDict[candidate]/total*100}% ({voteDict[candidate]})")
    if not(winner):
        winner=candidate
    else:
        if voteDict[candidate]>voteDict[winner]:
            winner=candidate


output=["Election Results","-------------------------",f"Total Votes: {total}",
"-------------------------","-------------------------",f"Winner: {winner}",
"-------------------------"]

output[4:4]=results
print(output)

