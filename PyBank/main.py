import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
content=[]
totalMonths=0
totalProfit=0
grtIncrease=0
grtDecrease=0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        content.append(row)
for row in content:
    totalMonths=totalMonths+1
    profit=int(row[1])
    totalProfit=totalProfit+profit
    if profit>grtIncrease:
        grtIncrease = profit
    elif profit<grtDecrease:
        grtDecrease = profit
averageChange=totalProfit/totalMonths
output=["Financial Analysis","----------------------------","Total Months: "+str(totalMonths),
"Total: "+str(totalProfit),"Average  Change: "+str(averageChange)]
for line in output:
    print(line)
    