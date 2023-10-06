# Main Script for PyPoll in Module 3 Python Challenge

import os
import csv

# Create path for csv file
csvpath = os.path.join('resources', 'election_data.csv')

Total_Votes = 0
Candidate_Counter = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header in the csv file
    csv_header = next(csvfile)
    
    # Create lists for the candidates and Votes
    Candidates = []
    Votes = []

    for row in csvreader:
        
        Total_Votes += 1 

        # Check if it's a new candidate and add to Candidate list
        if Candidates.count(row[2]) == 0:
            Candidates.append(row[2])
            Candidate_Counter += 1

        # Create list of every vote
        Votes.append(row[2])

# Create List of Vote Counts
Vote_Counts = []
for cans in Candidates:
    Vote_Counts.append(Votes.count(cans))

# Merge the Candidate list with Vote Counts together
Tallies = list(zip(Candidates, Vote_Counts))

# Find the winner
Winning_Votes = max(Vote_Counts)
Winner = Candidates[Vote_Counts.index(Winning_Votes)]

# Print Results to terminal
print("Election Results")
print("---------------------")
print(f"Total Votes: {Total_Votes}")
print("---------------------")
for cans in Tallies:
    percent = round((cans[1]/Total_Votes)*100, 3)
    print(f"{cans[0]}: {percent}% ({cans[1]})")
print("---------------------")
print(f"Winner: {Winner}")
print("---------------------")

# Write results to text file
with open("analysis/PyPoll_Output.txt", "w") as f:

    f.write("Election Results")
    f.write('\n')
    f.write("---------------------")
    f.write('\n')
    f.write(f"Total Votes: {Total_Votes}")
    f.write('\n')
    f.write("---------------------")
    f.write('\n')
    for cans in Tallies:
        percent = round((cans[1]/Total_Votes)*100, 3)
        f.write(f"{cans[0]}: {percent}% ({cans[1]})")
        f.write('\n')
    f.write("---------------------")
    f.write('\n')
    f.write(f"Winner: {Winner}")
    f.write('\n')
    f.write("---------------------")