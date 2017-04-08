
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
data_path = home_path+"\\Assignment 3\\Data"


# In[3]:

# Looping through each filename in above path and selecting the required file
for subdir,dirs, files in os.walk(data_path):
    for file in files:
        if file == 'vehicle_collisions.csv':
            data=pd.read_csv(os.path.join(subdir,file))
print(data.head(2))


# In[4]:

# Capturing only the required columns
new_DF = data[["BOROUGH","DATE","VEHICLE 1 TYPE","VEHICLE 2 TYPE","VEHICLE 3 TYPE","VEHICLE 4 TYPE","VEHICLE 5 TYPE"]].copy()
print(new_DF.head(2))


# In[5]:

# Formatting the date, Adding year to ease calculation
new_DF["DATE"]= pd.to_datetime(new_DF.DATE)
new_DF["YEAR"] = new_DF.DATE.dt.year
print(new_DF.head(5))


# In[6]:

# Putting 1 wherever vehicles involved in accidents and replacing NAN with 0

new_DF['VEHICLE 1 TYPE'] = new_DF['VEHICLE 1 TYPE'].str.replace('.*','1')
new_DF['VEHICLE 1 TYPE'] = new_DF['VEHICLE 1 TYPE'].fillna(0)

new_DF['VEHICLE 2 TYPE'] = new_DF['VEHICLE 2 TYPE'].str.replace('.*','1')
new_DF['VEHICLE 2 TYPE'] = new_DF['VEHICLE 2 TYPE'].fillna(0)

new_DF['VEHICLE 3 TYPE'] = new_DF['VEHICLE 3 TYPE'].str.replace('.*','1')
new_DF['VEHICLE 3 TYPE'] = new_DF['VEHICLE 3 TYPE'].fillna(0)

new_DF['VEHICLE 4 TYPE'] = new_DF['VEHICLE 4 TYPE'].str.replace('.*','1')
new_DF['VEHICLE 4 TYPE'] = new_DF['VEHICLE 4 TYPE'].fillna(0)

new_DF['VEHICLE 5 TYPE'] = new_DF['VEHICLE 5 TYPE'].str.replace('.*','1')
new_DF['VEHICLE 5 TYPE'] = new_DF['VEHICLE 5 TYPE'].fillna(0)

print(new_DF.head(5))


# In[7]:

# Considering accidents occurred only in 2015
new_DF = new_DF[(new_DF.YEAR >= 2015)].dropna(subset=["BOROUGH"])
print(new_DF.head(5))


# In[8]:

# Calculating the total accidents in each borough wherever a single vehicle is involved
vehicle1_DF = new_DF[["BOROUGH"]].copy()
vehicle1_DF["One_Vehicle_Involved"] = new_DF["VEHICLE 1 TYPE"].astype(str).astype(int)
vehicle1_DF = pd.DataFrame(vehicle1_DF.groupby("BOROUGH").One_Vehicle_Involved.sum().reset_index())
print(vehicle1_DF.head(5))


# In[9]:

# Calculating the total accidents in each borough wherever two vehicles are involved
vehicle2_DF = new_DF[["BOROUGH"]].copy()
vehicle2_DF["Two_Vehicle_Involved"] = new_DF["VEHICLE 2 TYPE"].astype(str).astype(int)
vehicle2_DF = pd.DataFrame(vehicle2_DF.groupby("BOROUGH").Two_Vehicle_Involved.sum().reset_index())
print(vehicle2_DF.head(5))


# In[10]:

# Calculating the total accidents in each borough wherever three vehicles are involved
vehicle3_DF = new_DF[["BOROUGH"]].copy()
vehicle3_DF["Three_Vehicle_Involved"] = new_DF["VEHICLE 3 TYPE"].astype(str).astype(int)
vehicle3_DF = pd.DataFrame(vehicle3_DF.groupby("BOROUGH").Three_Vehicle_Involved.sum().reset_index())
print(vehicle3_DF.head(5))


# In[11]:

# Calculating the total accidents in each borough wherever four vehicles are involved
vehicle4_DF = new_DF[["BOROUGH"]].copy()
vehicle4_DF["Four_Vehicle_Involved"] = new_DF["VEHICLE 4 TYPE"].astype(str).astype(int)
vehicle4_DF = pd.DataFrame(vehicle4_DF.groupby("BOROUGH").Four_Vehicle_Involved.sum().reset_index())
print(vehicle4_DF.head(5))


# In[12]:

# Calculating the total accidents in each borough wherever five vehicles are involved
vehicle5_DF = new_DF[["BOROUGH"]].copy()
vehicle5_DF["Five_Vehicle_Involved"] = new_DF["VEHICLE 5 TYPE"].astype(str).astype(int)
vehicle5_DF = pd.DataFrame(vehicle5_DF.groupby("BOROUGH").Five_Vehicle_Involved.sum().reset_index())
print(vehicle5_DF.head(5))


# In[13]:

# Merging the total accidents categorywise in each borough into a single dataframe

final_DF = pd.merge(vehicle1_DF,vehicle2_DF,on ='BOROUGH' , how='inner')
final_DF.columns = ["BOROUGH","One_Vehicle_Involved","Two_Vehicle_Involved"]

final_DF = pd.merge(final_DF,vehicle3_DF,on ='BOROUGH' , how='inner')
final_DF.columns = ["BOROUGH","One_Vehicle_Involved","Two_Vehicle_Involved","Three_Vehicle_Involved"]

final_DF = pd.merge(final_DF,vehicle4_DF,on ='BOROUGH' , how='inner')
final_DF.columns = ["BOROUGH","One_Vehicle_Involved","Two_Vehicle_Involved","Three_Vehicle_Involved","Four_Vehicle_Involved"]

final_DF = pd.merge(final_DF,vehicle5_DF,on ='BOROUGH' , how='inner')
final_DF.columns = ["BOROUGH","One_Vehicle_Involved","Two_Vehicle_Involved","Three_Vehicle_Involved","Four_Vehicle_Involved","Five_Vehicle_Involved"]


print(final_DF.head(2))


# In[14]:

# Calculating the number of accidents involving four vehicles
final_DF["Four_Vehicle_Involved"] = final_DF["Four_Vehicle_Involved"] - final_DF["Five_Vehicle_Involved"]


# In[15]:

# Calculating the number of accidents involving three vehicles
final_DF["Three_Vehicle_Involved"] = (final_DF["Three_Vehicle_Involved"] - final_DF["Four_Vehicle_Involved"])-final_DF["Five_Vehicle_Involved"]


# In[16]:

# Calculating the number of accidents involving two vehicles
final_DF["Two_Vehicle_Involved"] = ((final_DF["Two_Vehicle_Involved"]-final_DF["Three_Vehicle_Involved"])-final_DF["Four_Vehicle_Involved"])-final_DF["Five_Vehicle_Involved"]                     


# In[17]:

# Calculating the number of accidents involving one vehicle
final_DF["One_Vehicle_Involved"]=(((final_DF["One_Vehicle_Involved"]-final_DF["Two_Vehicle_Involved"])-final_DF["Three_Vehicle_Involved"])-final_DF["Four_Vehicle_Involved"])- final_DF["Five_Vehicle_Involved"]


# In[18]:

# Creating a dataframe combining the four and five vehicles accidents cases alongwith one, two and three vehicles accidents
final_output_DF = final_DF
final_output_DF["Extra_Vehicles_involved"] = final_output_DF["Four_Vehicle_Involved"] + final_output_DF["Five_Vehicle_Involved"]
final_output_DF.drop('Four_Vehicle_Involved', axis=1, inplace=True)
final_output_DF.drop('Five_Vehicle_Involved', axis=1, inplace=True)

print(final_output_DF.head(5))


# In[19]:

# Creating a function to create a csv file to save the above captured data
def save_to_CSV():
    if not os.path.exists(home_path+"\\Assignment 3\\Output\\Q1_Part_2"):
        os.makedirs(home_path+"\\Assignment 3\\Output\\Q1_Part_2")
    
    with open(home_path+'\\Assignment 3\\Output\\Q1_Part_2\\Q1_Part_2.csv', 'w') as myfile:
        myfile.write(final_output_DF.to_csv(index=False))

# Calling the function
save_to_CSV()

