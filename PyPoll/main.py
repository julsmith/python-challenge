# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:19:46 2019

@author: julsmith
"""

import os
import csv
# find csv path 
pybank_csv = os.path.join("PyPoll_resources_election_data.csv")

# read file 
with open(pybank_csv, "r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    total_votes = len(data)-1
 
   
# creates dictionary 
i = 1
unique_list_array = {}
while i<len(data):
    names = str(data[i][2])
    if names not in unique_list_array:
        unique_list_array[names] = 1
    else:
        unique_list_array[names] = unique_list_array[names]+1
    i += 1 
unique_values = unique_list_array
print(unique_values)

## out of the dictionary get winner
winner_list = max(unique_list_array.items(), key=lambda k: k[1])
winner = winner_list[0]


win_candidate = ""
winning_votes = 0
final_list = []
unique_candidates = ""
percent = ""
votes_final = "votes"

for result in unique_list_array:
   votes = unique_list_array.get(result)
   percent = float(votes)/float(total_votes)* 100
   unique_candidates = (f"{result}:  {percent:.3f}% ({votes})")
   final_list.append(unique_candidates)
   if votes > winning_votes:
       winning_votes = votes
       win_candidate = result

## write file to the txt file
final_summary  = "\n".join(final_list)
print(final_summary)

file = open("results.txt", "w")
file.write("Election Results \n")

print("Elections Results")
print("-------------------")
file.write("-------------------\n")
print("Total Votes: " + str(total_votes))
file.write("Total Votes: " + str(total_votes)+"\n")
print("-------------------")
file.write("-------------------\n")
print(final_summary + "\n")
file.write(final_summary + "\n")
print("-------------------")
file.write("-------------------\n")
print("Winner: " + str(winner))
file.write("Winner:"+ str(winner)+"\n")
print("-------------------")
file.write("-------------------\n")
file.close() 
 



   