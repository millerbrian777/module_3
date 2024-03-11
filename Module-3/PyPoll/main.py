import os
import csv

dirname = os.path.dirname(__file__)
election_data= os.path.join(dirname, "Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}


with open(election_data, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

print("Total Votes:", total_votes)
print("\nCandidates who received votes:")
for candidate in candidate_votes:
    print(candidate)
    print("  Votes:", candidate_votes[candidate])
    print("  Percentage of Votes: {:.2f}%".format(percentage_votes[candidate]))
    
print("\nWinner:", winner)