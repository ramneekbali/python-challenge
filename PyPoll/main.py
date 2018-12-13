import os
import csv
from collections import Counter
import sys
poll_data = os.path.join('/Users/p2778494/UDEN201811DATA3/Week3/HW/Instructions/PyPoll/Resources','election_data.csv')

Voter_ID_list=[]
County_list=[]
Candidate_list=[]
print("Election Results")
print("---------------------------------")
with open(poll_data,'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
       Voter_ID_list.append(row[0])
    for row in reader:
       Candidate_list.append(row[2])




Total_votes =len(Voter_ID_list)
print("Total Votes:", Total_votes)
print("---------------------------------")

with open(poll_data,'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
       Candidate_list.append(row[2])


Candidate_count=dict(Counter(Candidate_list))
#print(type(Candidate_count))
Candidate_summary={k:v/len(Voter_ID_list) for k,v in Candidate_count.items()}
for k,v in Candidate_summary.items():
    print(f"{k} : {round(v*100,3)}% ({round(v*len(Voter_ID_list))})")
print("---------------------------------")

winner_count=max(Candidate_count.values())
winner_name=[k for k,v in Candidate_count.items() if v==winner_count]
for winner in winner_name:
    print(f"Winner: {winner}")
print("---------------------------------")

output_file = os.path.join("output_poll.csv")
output=open("output_poll.csv", "w")

print("Election Results",file=output)
print("---------------------------------",file=output)
print("Total Votes:", Total_votes,file=output)
print("---------------------------------",file=output)
for k,v in Candidate_summary.items():
    print(f"{k} : {round(v*100,3)}% ({round(v*len(Voter_ID_list))})",file=output)
print("---------------------------------",file=output)
for winner in winner_name:
    print(f"Winner: {winner}",file=output)
print("---------------------------------",file=output)
