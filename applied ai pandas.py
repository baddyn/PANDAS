
# coding: utf-8

# In[5]:


import pandas as pd
df=pd.read_csv('nyc_weather.csv')
df #df is the data frame or basicallly table which is contained in csv files


# In[3]:


#to get max temperature
df['Temperature'].max()


# In[6]:


#to know which day it rains
df["EST"][df["Events"]=='Rain']


# In[7]:


#avg wind speed
df["WindSpeedMPH"].mean()


# In[8]:


#to do above 4 operations without pandas would have taken aroud 50+lines


# In[9]:


#data frame basics
# adat frame is main object in pandas
#used to represent rows and xolumns
#that is to represent tabular or excel spreadsheet
#csv stored as comma seperated values

import pandas as pd
df=pd.read_csv("weather_data.csv")
df


# In[10]:


df.shape #total rows and coln


# In[11]:


df.head #first few rows


# In[12]:


df.tail #last few rows


# In[14]:


df[2:5] #slicing row 2,3,4


# In[15]:


df.columns


# In[16]:


#to pick one column
df['day']


# In[17]:


#method 2
df.day


# In[18]:


#for 2 columns
df[['day','event']]


# df.temperature

# In[22]:


df['temperature'].min()


# In[24]:


df['temperature'].describe()
#idea of what data looks like


# In[25]:


#select row with max temp
#important
#bit like sql
df[df.temperature==df.temperature.max()]


# In[26]:


#if want only day of above so
df.day[df.temperature==df.temperature.max()]


# In[27]:


#PART 3 OF VIDEOS
#VERY IMPORTANT


# In[28]:


#XLS FILES ARE XL FILES 
#CSV ARE COMMA SEERATED VALUES
#AS XL FILES ARE USED TO STORE TABLES
#WE WORK WITH XLS IN PANDAS


#FOR XL FILES

df=pd.read_excel('weather_data.xlsx')
df


# In[29]:


#write data to csv 
df.to_csv('new.csv') #will create the file if it doesnt exist
#this also stores index of row

#to not store the index
df.to_csv('new_noindex',index=False)


# In[32]:


#write data to excel

#in a excel file we can have multiple sheets
#so specify sheet name
#a sheet si simpy a table
df.to_excel('new.xlsx',sheet_name='weather_data')


# In[39]:


df=pd.read_csv('weather_data_cities.csv')
df


# In[44]:


#imp operators on df

g=df.groupby('city')
g
#groups accoring to city in the original table
df
#as can be seen below just like sql


# In[48]:


for city,city_df in g:
    print(city)
    print(city_df)
    #index is accd to original list
    


# In[49]:


g.describe()


# In[50]:


g.mean()


# In[51]:


g.max()


# In[52]:


g.get_group('mumbai')


# In[53]:


#to concatenate two data frames

#df=pd.concat({name1,name2},ignore_index=True)
#index statement will remove indexe of df from original df

#to concat row wise 
#jsut set axis =1


# In[54]:


#merging dataframes

#just like sql join

#df=pd.merge(df1,df2,on='city')
#city is common attribute

#lets say for a city x its record is in df1 but not in df2  it 
#will be dropped form df


#to prevet this 
#perform outer join

#df=pd.merge(df1,df2,on='city',how='outer')
#the values for non available values is nan


# In[56]:


#indexing

df=pd.DataFrame([1,2,3,4],index=[100,200,300,400])
#now 1st element will have index and so on
df


# In[62]:


#now we want to find two things
#1. df at  200
#2. df at row 2

#loc and iloc commands

#using index use loc
df.loc[200]

#for using row no.
df.iloc[2]




# In[63]:


df.loc[:300]
#values till index 300


# In[65]:


df.iloc[:2]
#tilll row 2

