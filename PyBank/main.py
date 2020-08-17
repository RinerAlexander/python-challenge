import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
outputpath = os.path.join('analysis', 'output.txt')
content=[]
totalMonths=0
totalProfit=0
grtIncrease=0
grtInMonth="No Increase in Profits"
grtDecrease=0
grtDeMonth="No Decrease in Profits"

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
        grtInMonth = row[0]
    elif profit<grtDecrease:
        grtDecrease = profit
        grtDeMonth = row[0]
averageChange=totalProfit/totalMonths
output=["Financial Analysis","----------------------------","Total Months: "+str(totalMonths),
"Total: "+str(totalProfit),"Average  Change: "+str(averageChange),
f"Greatest Increase in Profits: {grtInMonth} ({grtIncrease})",
f"Greatest Decrease in Profits: {grtDeMonth} ({grtDecrease})"]
for line in output:
    print(line)
    txtOutput = open(outputpath,"a") 
    txtOutput.write(line+"\n")
    txtOutput.close() 

    