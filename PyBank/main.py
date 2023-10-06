# Main Script for PyBank in Module 3 Python Challenge

import os
import csv

# Create path for csv file
csvpath = os.path.join('resources', 'budget_data.csv')

# Initialize the necessary tracking numbers
num_Months = 0
profit_Net = 0
prev_row = 0
row_Counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header in the csv file
    csv_header = next(csvfile)
    
    # Create lists for the monthly changes in profit and the date
    changes_Profit = []
    Date = []

    for row in csvreader:
        
        row_Counter += 1

        # Count rows
        num_Months += 1    

        # Net total amount of profit/losses over period
        profit_Net = profit_Net + int(row[1])

        Date.append(row[0])

        # Changes in profits/losses over entire period
        if row_Counter > 1:
            difference = int(row[1]) - prev_row
            changes_Profit.append(difference)

        prev_row = int(row[1])

# Calculate the average change
average_change = round(sum(changes_Profit)/len(changes_Profit), 2)

# Find the max increase and decrease
Greatest_Increase = max(changes_Profit)
Increase_Index = changes_Profit.index(Greatest_Increase)
Increase_Date = Date[Increase_Index+1]

Greatest_Decrease = min(changes_Profit)
Decrease_Index = changes_Profit.index(Greatest_Decrease)
Decrease_Date = Date[Decrease_Index+1]

# Print analysis to terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {num_Months}")
print(f"Total: = ${profit_Net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {Increase_Date} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Decrease_Date} (${Greatest_Decrease})")

# Write analysis to text file
with open("analysis/PyBank_Output.txt", "w") as f:

    f.write("Financial Analysis")
    f.write('\n')
    f.write("-------------------------")
    f.write('\n')
    f.write(f"Total Months: {num_Months}")
    f.write('\n')
    f.write(f"Total: = ${profit_Net}")
    f.write('\n')
    f.write(f"Average Change: ${average_change}")
    f.write('\n')
    f.write(f"Greatest Increase in Profits: {Increase_Date} (${Greatest_Increase})")
    f.write('\n')
    f.write(f"Greatest Decrease in Profits: {Decrease_Date} (${Greatest_Decrease})")

