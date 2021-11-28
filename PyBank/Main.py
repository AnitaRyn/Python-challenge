#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv

csv_filepath = "budget_data.csv"

with open(csv_filepath, "r", newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    columns = reader.fieldnames
    # Lists for each column
    lists = {column: [] for column in columns}  

    for row in reader:
        for column in columns[0:]:
            lists[column].append(str(row[column]))

    for row in reader:
        for column in columns[1:]:
            lists[column].append(int(row[column]))
            
    for column_name, column in lists.items():
        print(f'{column_name}: {column}')
        


# In[3]:


length = len(lists['Date'])
print(length)


# In[ ]:


sum = sum(lists['Profit/Losses'])
print(sum)


# In[ ]:




