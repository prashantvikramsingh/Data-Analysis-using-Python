
# coding: utf-8

# In[2]:

# Importing all required modules
import os
from os import listdir
from os.path import isfile, join
import glob
import csv
import pandas as pd
import calendar
import re


# In[3]:

# Creating the path to read the input file
home_path = os.path.expanduser("~")
data_path = home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Data"


# In[4]:

# Looping through each filename in above path and selecting the required file
for subdir,dirs, files in os.walk(data_path):
    for file in files:
        if file == 'movies_awards.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[5]:

# Capturing only required columns
temp_DF = data[["Title","Awards"]].copy()
print(temp_DF.head(10))


# In[6]:

# Removing NAN from above data
temp_DF=temp_DF.dropna(subset=['Awards'])
print(temp_DF.head(10))


# # Using REGX  separating the count

# In[7]:

#calculating all sentences with pattern 2 win or 3 win
temp_DF["Awards_won"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"(\d+) win", x)))
# Finding the 0th element of array
temp_DF["Awards_won"] = temp_DF["Awards_won"].apply(lambda x : [0] if len(x)==0 else x) 
# Converting to integer
temp_DF["Awards_won"] = temp_DF["Awards_won"].apply(lambda x : list(map(int,x))[0])

# Doing this for all award categories with respective pattern 

temp_DF["Awards_Nominated"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"(\d+) nominations", x)))
temp_DF["Awards_Nominated"] = temp_DF["Awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Awards_Nominated"] = temp_DF["Awards_Nominated"].apply(lambda x : list(map(int,x))[0])

temp_DF["Golden_glob_awards_won"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Golden ", x)))
temp_DF["Golden_glob_awards_won"] = temp_DF["Golden_glob_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Golden_glob_awards_won"] = temp_DF["Golden_glob_awards_won"].apply(lambda x : list(map(int,x))[0])

temp_DF["Golden_glob_awards_Nominated"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Golden ", x)))
temp_DF["Golden_glob_awards_Nominated"] = temp_DF["Golden_glob_awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Golden_glob_awards_Nominated"] = temp_DF["Golden_glob_awards_Nominated"].apply(lambda x : list(map(int,x))[0])


# In[8]:

temp_DF["Oscar_awards_Nominated"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Oscar", x)))
temp_DF["Oscar_awards_Nominated"] = temp_DF["Oscar_awards_Nominated"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Oscar_awards_Nominated"] = temp_DF["Oscar_awards_Nominated"].apply(lambda x : list(map(int,x))[0])


# In[9]:

temp_DF["Oscar_Won"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Oscar", x)))
temp_DF["Oscar_Won"] = temp_DF["Oscar_Won"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Oscar_Won"] = temp_DF["Oscar_Won"].apply(lambda x : list(map(int,x))[0])


# In[10]:

temp_DF["Prime_awards_nominated"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) Primetime", x)))
temp_DF["Prime_awards_nominated"] = temp_DF["Prime_awards_nominated"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Prime_awards_nominated"] = temp_DF["Prime_awards_nominated"].apply(lambda x : list(map(int,x))[0])


# In[11]:

temp_DF["Prime_awards_won"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Won (\d+) Primetime", x)))
temp_DF["Prime_awards_won"] = temp_DF["Prime_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["Prime_awards_won"] = temp_DF["Prime_awards_won"].apply(lambda x : list(map(int,x))[0])


# In[12]:

temp_DF["BAFTA_awards_nominated"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Nominated for (\d+) BAFTA", x)))
temp_DF["BAFTA_awards_nominated"] = temp_DF["BAFTA_awards_nominated"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["BAFTA_awards_nominated"] = temp_DF["BAFTA_awards_nominated"].apply(lambda x : list(map(int,x))[0])


# In[13]:

temp_DF["BAFTA_awards_won"] = temp_DF["Awards"].apply(lambda x : (re.findall(r"Won (\d+) BAFTA", x)))
temp_DF["BAFTA_awards_won"] = temp_DF["BAFTA_awards_won"].apply(lambda x : [0] if len(x)==0 else x)
temp_DF["BAFTA_awards_won"] = temp_DF["BAFTA_awards_won"].apply(lambda x : list(map(int,x))[0])


# In[14]:

# Adding all awards counts to get the awards won and awards nominated
temp_DF["Awards_won"] = ((((temp_DF["Awards_won"] + temp_DF["Golden_glob_awards_won"]) + temp_DF["Oscar_Won"]) + temp_DF["Prime_awards_won"]) + temp_DF["BAFTA_awards_won"])
temp_DF["Awards_Nominated"] = ((((temp_DF["Awards_Nominated"] + temp_DF["Golden_glob_awards_Nominated"]) + temp_DF["Oscar_awards_Nominated"]) + temp_DF["Prime_awards_nominated"]) + temp_DF["BAFTA_awards_nominated"])
print(temp_DF.head(5))


# In[15]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q4_Part_1"):
        os.makedirs(home_path+"\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q4_Part_1")
    
    with open(home_path+'\\Downloads\\Documents\\Data Analysis Python\\DAUP_2017\\Assignment_PVS\\Assignment 3\\Output\\Q4_Part_1\\Q4_Part_1.csv', 'w') as myfile:
        myfile.write(temp_DF.to_csv(index=False))
        
# Calling the function
save_to_CSV()

