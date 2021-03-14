import csv
import os

#Opening resrouces folder
cvspath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")


#In python, unfortunately, values/ data types are defined by the "=" operator
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenueChange = 0
revenueList = []
monthlyChange = []

#Labeling Min to the number 0, as the smallest "increase" would be no increase
greatestIncrease = ["", 0]

#Labeling Max to the number that stack overflow told me would be a good number
greatestDecrease = ["", 99999999999]

#Opening a file as RevenueData
with open(cvspath) as revenueData:
   reader = csv.DictReader(revenueData)

#I need to loop through the data to collect the answers
   for row in reader:

       #Totaling
           totalMonth = totalMonth + 1
           totalRevenue += int(row["Revenue"])

#Calculating change in revenue
           revenueChange = int(row["Revenue"]) - previousRevenue
           previousRevenue = int(row["Revenue"])
           monthlyChange = monthlyChange + [row["Date"]]

           #Greatest Increase value
           if (revenueChange > greatestIncrease[1]):
               greatestIncrease[1] = revenueChange
               greatestIncrease[0] = row["Date"]

           if (revenueChange < greatestDecrease[1]):
               greatestDecrease[0] = row["Date"]
               greatestDecrease[1] = revenueChange
        
#The Total sum divided the total number of values
revenueAvg = sum(revenueList) / len(revenueList)


#Printing results
output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenueAvg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)

print(output)

#Updating the txtFile
with open(pathout, "w") as txtFile:
    txtFile.write(output)
