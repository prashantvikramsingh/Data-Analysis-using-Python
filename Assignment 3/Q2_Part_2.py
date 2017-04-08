
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
data_path = home_path+"\\Assignment 3\\Data"


# In[3]:

# Looping through each filename in above path and selecting the required file
for subdir,dirs, files in os.walk(data_path):
    for file in files:
        if file == 'employee_compensation.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[4]:

# Capturing the required columns
emp_DF = data[["Year Type","Employee Identifier","Job Family","Salaries","Overtime","Total Benefits","Total Compensation"]].copy()
print(emp_DF.head(2))


# In[5]:

# Considering only those employees where year type is Calendar
emp_DF = emp_DF[(emp_DF['Year Type'] == 'Calendar')]
print(emp_DF.head(5))


# In[6]:

# Calculating mean of the total compensation based on employee identifier
emp_DF_total_compenstn = emp_DF.groupby('Employee Identifier', as_index=False)['Total Compensation'].mean()
print(emp_DF_total_compenstn.head(5))


# In[7]:

# Calculating mean of the total benefits based on employee identifier
emp_DF_total_benefit = emp_DF.groupby('Employee Identifier', as_index=False)['Total Benefits'].mean()
print(emp_DF_total_benefit.head(5))


# In[8]:

# Merging the above two mean data in a single dataframe based on employee identifier
final_DF = pd.merge(emp_DF_total_compenstn,emp_DF_total_benefit,on ='Employee Identifier' , how='inner')
final_DF.columns = ["Employee Identifier","Total Compensation","Total Benefits"]
print(final_DF.head(5))


# In[9]:

# Calculating the actual salaries based on overtime the an employee did
salaries_DF = emp_DF[(emp_DF['Overtime'] > 0.05 * emp_DF['Salaries'])]
print(salaries_DF.head(5))


# In[10]:

# Capturing only the required columns from above output
job_family_DF = salaries_DF[["Job Family","Total Benefits","Total Compensation"]].copy()
print(job_family_DF.head(5))


# In[11]:

# Calculating mean of total benefits at each Job Family level
job_family_total_benefits = job_family_DF.groupby('Job Family', as_index=False)['Total Benefits'].mean()
print(job_family_total_benefits.head(5))


# In[12]:

# Calculating mean of total compensation at each Job Family level
job_family_total_compenstn = job_family_DF.groupby('Job Family', as_index=False)['Total Compensation'].mean()
print(job_family_total_compenstn.head(5))


# In[13]:

# Merging the above two outputs based on Job Family
final_job_family_DF = pd.merge(job_family_total_benefits,job_family_total_compenstn,on ='Job Family' , how='inner')
final_job_family_DF.columns = ["Job Family","Total Benefits","Total Compensation"]
print(final_job_family_DF.head(5))


# In[14]:

# Calculating the percentage of total benefits to total compensation
final_job_family_DF["Percentage"] = (final_job_family_DF['Total Benefits']/ final_job_family_DF['Total Compensation'])*100
print(final_job_family_DF.head(5))


# In[15]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Assignment 3\\Output\\Q2_Part_2"):
        os.makedirs(home_path+"\\Assignment 3\\Output\\Q2_Part_2")
    
    with open(home_path+'\\Assignment 3\\Output\\Q2_Part_2\\Q2_Part_2.csv', 'w') as myfile:
        myfile.write(final_job_family_DF.to_csv(index=False))
        
# Calling the function
save_to_CSV()

