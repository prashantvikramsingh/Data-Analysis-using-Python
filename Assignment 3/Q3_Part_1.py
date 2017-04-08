
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
        if file == 'cricket_matches.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[4]:

# Capturing only the required columns
cric_match_details_DF = data[["home","away","winner","innings1","innings1_runs","innings2","innings2_runs"]].copy()
print(cric_match_details_DF.head(5))


# In[5]:

# Capturing only those records where home match was won
home_match_winners_DF = cric_match_details_DF[(cric_match_details_DF['home'] == cric_match_details_DF['winner'])]
print(home_match_winners_DF.head(5))


# In[7]:

# Capturing only those records where home team batted first
home_match_first_inning = home_match_winners_DF[["home","innings1","innings1_runs"]].copy()
home_match_first_inning = home_match_first_inning[(home_match_first_inning['home'] == home_match_first_inning['innings1'])]


# In[8]:

# Calculating mean of innings run from above result
home_match_first_inning = home_match_first_inning.groupby('home', as_index=False)['innings1_runs'].mean()
print(home_match_first_inning.head(5))


# In[9]:

# Capturing only those records where home team batted second
home_match_second_inning = home_match_winners_DF[["home","innings2","innings2_runs"]].copy()
home_match_second_inning = home_match_second_inning[(home_match_second_inning['home'] == home_match_second_inning['innings2'])]


# In[10]:

# Calculating mean of innings run from above result
home_match_second_inning = home_match_second_inning.groupby('home', as_index=False)['innings2_runs'].mean()
print(home_match_second_inning.head(5))


# In[11]:

# Merging the above two results based on home
complete_inning_DF = pd.merge(home_match_first_inning,home_match_second_inning,on ='home' , how='outer')
complete_inning_DF.columns = ["home","First_inning_avg","Second_inning_avg"]
print(complete_inning_DF.head(5))


# In[12]:

# Calculating the mean of first and second innings
complete_inning_DF["Score"] = complete_inning_DF[["First_inning_avg","Second_inning_avg"]].mean(axis=1)


# In[13]:

# Displaying the mean based on home
complete_inning_DF.drop('First_inning_avg', axis=1, inplace=True)
complete_inning_DF.drop('Second_inning_avg', axis=1, inplace=True)
complete_inning_DF["Score"] = complete_inning_DF["Score"].apply(np.int64)
print(complete_inning_DF.head(5))


# In[14]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q3_Part_1"):
        os.makedirs(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q3_Part_1")
    
    with open(home_path+'\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q3_Part_1\\Q3_Part_1.csv', 'w') as myfile:
        myfile.write(complete_inning_DF.to_csv(index=False))
        
# Calling the function
save_to_CSV()

