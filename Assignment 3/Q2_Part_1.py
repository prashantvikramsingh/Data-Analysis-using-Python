
# coding: utf-8

# In[1]:

# Importing all required modules
import os
from os import listdir
from os.path import isfile, join
import glob
import csv
import pandas as pd
import calendar
import numpy as np


# In[2]:

# Creating the path to read the input file
home_path = os.path.expanduser("~")
data_path = home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Data"


# In[3]:

# Looping through each filename in above path and selecting the required file
for subdir,dirs, files in os.walk(data_path):
    for file in files:
        if file == 'employee_compensation.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[4]:

# Capturing the required columns
new_DF = data[["Organization Group","Department","Total Compensation"]].copy()
print(new_DF.head(2))


# In[6]:

# Calculating the mean at Organization Group and Department
mean_DF = new_DF[["Organization Group","Department","Total Compensation"]].copy()
mean_DF = mean_DF.groupby(['Organization Group','Department'])['Total Compensation'].mean()
mean_DF= pd.DataFrame(mean_DF)
print(mean_DF.head(5))


# In[7]:

# Sorting the above calculated mean
temp = mean_DF['Total Compensation'].groupby(level=0, group_keys=False)
sorted_DF = temp.apply(lambda x: x.order(ascending=False))

sorted_DF = pd.DataFrame(sorted_DF)
print(sorted_DF.head(20))


# In[8]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q2_Part_1"):
        os.makedirs(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q2_Part_1")
    
    with open(home_path+'\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q2_Part_1\\Q2_Part_1.csv', 'w') as myfile:
        myfile.write(sorted_DF.to_csv(index=False))

# Calling the function
save_to_CSV()

