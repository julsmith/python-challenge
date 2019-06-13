# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:19:37 2019

@author: julsmith
"""

import os
import csv
## find csv path 
pybank_csv = os.path.join("python-challenge","PyBank","Pybank_budget_data.csv")
## read the file
with open(pybank_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    ## print file 
with open(pybank_csv, 'r') as text:
    print(text)
    lines = text.read()
    print(lines)    

def print_data(PyBank_data):
    date = int(PyBank_data[0])
    profit_losses = int(PyBank_dat[1])
    
    ## get number of rows = months
    
with open(pybank_csv, "r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)-1
    print(row_count)
    
total_months = (row_count)
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(total_months))

with open(pybank_csv) as fin:
    total = sum(int(r[1] for r in csv.reader(fin))
    