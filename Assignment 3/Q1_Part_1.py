
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


# In[2]:

# Creating the path to read the input file
home_path = os.path.expanduser("~")
data_path = home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Data"


# In[4]:

# Looping through each filename in above path and selecting the required file
for subdir,dirs, files in os.walk(data_path):
    for file in files:
        if file == 'vehicle_collisions.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[5]:

# Formatting the date, adding month and year to ease calculation
data["DATE"] = pd.to_datetime(data.DATE)
data["MONTH"] = data.DATE.dt.month
data["MONTH"] = data["MONTH"].apply(lambda x: calendar.month_abbr [x])
data["YEAR"] = data.DATE.dt.year
print(data.head(2))


# In[6]:

# Counting monthwise the total accidents in 2016 in Manhattan
data["COUNT"] = 1
Manhattan_DF = pd.DataFrame(data[(data.YEAR == 2016) & (data.BOROUGH == "MANHATTAN")].groupby("MONTH").COUNT.sum().reset_index())
print(Manhattan_DF.head(2))


# In[8]:

# Counting monthwise the total accidents in New York
NYC_DF = pd.DataFrame(data[(data.YEAR == 2016)].groupby("MONTH").COUNT.sum().reset_index())
print(NYC_DF.head(2))


# In[9]:

# Merging the above two data based on month
total_DF = pd.merge(Manhattan_DF, NYC_DF , on ='MONTH' , how='inner')
total_DF.columns = ["MONTH","MANHATTAN","NEWYORK"]
print(total_DF.head(2))


# In[11]:

# Calculating the accident percentage for each month
total_DF["Percentage"] = (total_DF.MANHATTAN / total_DF.NEWYORK)
print(total_DF.head(2))


# In[12]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q1_Part_1"):
        os.makedirs(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q1_Part_1")
    
    with open(home_path+'\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q1_Part_1\\Q1_Part_1.csv', 'w') as myfile:
        myfile.write(total_DF.to_csv(index=False))
        
# Calling the function        
save_to_CSV()

