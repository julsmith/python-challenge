# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:34:00 2019

@author: julsmith
"""
import os
import csv
## find csv path 
pybank_csv = os.path.join("Pybank_budget_data.csv")


# read file 
with open(pybank_csv, "r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    ## calculate total months
    row_count = len(data)-1
    #print(data)
    
    total = len(data)-1
    #print(total)
    
index = 0
sum = 0
sum_of_average = 0
i = 1
difference = 0
difference_array = []
while i<len(data):
    ## print(i)
    ## print(data[i][1])
    sum += int(data[i][1])
    if i+1 <= total:
        difference = int(data[i+1][1]) - int(data[i][1])      
        print(difference)
        difference_array.append(difference)
        sum_of_average += difference        
    i += 1
    
#print(sum)

#print(sum_of_average/(total-1)) 
#print(difference_array)
max_val = max(difference_array)
max_index = difference_array.index(max_val)
min_val = min(difference_array)
min_index = difference_array.index(min_val)

file = open("results.txt", "w")
file.write("Financial Analysis\n")
print("Financial Analysis")
print("-------------------")
file.write("-------------------\n")
print("Total Months: " + str(total))
file.write("Total Months: " + str(total)+"\n")
print("Total: " + str(sum))
file.write("Total: " + str(sum)+"\n")
print("Average Change: " + str(sum_of_average))
file.write("Average Change: " + str(sum_of_average)+"\n")
print("Greatest Increase in Profits: " +  str(data[max_index+2][0]) + " ($" +(str(max_val)) + ")" )
file.write("Greatest Increase in Profits: " +  str(data[max_index+2][0]) + " ($" +(str(max_val)) + ")\n" )
print("Greatest Decrease in Profits: " +  str(data[min_index+2][0]) + " ($" +(str(min_val)) + ")" )
file.write("Greatest Decrease in Profits: " +  str(data[min_index+2][0]) + " ($" +(str(min_val)) + ")\n" ) 
 
file.close() 

    
    