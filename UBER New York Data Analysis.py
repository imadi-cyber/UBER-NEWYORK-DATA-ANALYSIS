#!/usr/bin/env python
# coding: utf-8

# Collect Data for Analysis

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df1 = pd.read_csv("uber-raw-data-apr14.csv")


# In[4]:


df2 = pd.read_csv("uber-raw-data-may14.csv")


# In[5]:


df3 = pd.read_csv("uber-raw-data-jun14.csv")


# In[6]:


df4 = pd.read_csv("uber-raw-data-jul14.csv")


# In[7]:


df5 = pd.read_csv("uber-raw-data-aug14.csv")


# In[8]:


df6 = pd.read_csv("uber-raw-data-sep14.csv")


# In[9]:


df1 = df1.append(df2, ignore_index=True)


# In[10]:


df1 = df1.append(df3, ignore_index=True)


# In[11]:


df1 = df1.append(df4, ignore_index=True)


# In[12]:


df1 = df1.append(df5, ignore_index=True)


# In[13]:


df1 = df1.append(df6, ignore_index=True)


# In[14]:


df1


# In[15]:


df1.shape


# Data Preparation

# In[16]:


df = df1.copy()


# In[17]:


df.head()


# In[18]:


df.dtypes


# In[19]:


df["Date/Time"] = pd.to_datetime(df["Date/Time"])


# In[20]:


df.dtypes


# In[21]:


df["weekday"] = df["Date/Time"].dt.day_name()
df["day"] = df["Date/Time"].dt.day
df["minute"] = df["Date/Time"].dt.minute
df["hour"] = df["Date/Time"].dt.hour
df["month"] = df["Date/Time"].dt.month


# In[22]:


df


# Analyzing Trips of Uber

# In[23]:


#analyzing number of trips on weekdays
weekdays = df["weekday"].value_counts()
weekdays


# In[24]:


weekdays.plot.bar()


# In[25]:


#analyzing number of trips in months
months = df["month"].value_counts()
months


# In[26]:


months.plot.bar()


# In[27]:


#analyzing number of trips on different days
days = df["day"].value_counts()
days


# In[28]:


days.plot.bar(figsize=(16,8))


# In[29]:


#analyzing number of trips on different hours of the day
hours = df["hour"].value_counts()
hours


# In[30]:


hours.plot.bar(figsize=(16,8))


# In[31]:


dfapril = df[df["month"] == 4]
dfaprilcount = dfapril["weekday"].value_counts()

dfmay = df[df["month"] == 5]
dfmaycount = dfmay["weekday"].value_counts()

dfjune = df[df["month"] == 6]
dfjunecount = dfjune["weekday"].value_counts()

dfjuly = df[df["month"] == 7]
dfjulycount = dfjuly["weekday"].value_counts()

dfaugust = df[df["month"] == 8]
dfaugustcount = dfaugust["weekday"].value_counts()

dfsept = df[df["month"] == 9]
dfseptcount = dfsept["weekday"].value_counts()


# In[32]:


fig, ax = plt.subplots(3,2)
april = dfaprilcount.plot.bar(ax=ax[0,0], figsize=(16,8))
april.set_title("April")
may = dfmaycount.plot.bar(ax=ax[0,1], figsize=(16,8))
may.set_title("May")
june = dfjunecount.plot.bar(ax=ax[1,0], figsize=(16,8))
june.set_title("June")
july = dfjulycount.plot.bar(ax=ax[1,1], figsize=(16,8))
july.set_title("July")
august = dfaugustcount.plot.bar(ax=ax[2,0], figsize=(16,8))
august.set_title("August")
sept = dfseptcount.plot.bar(ax=ax[2,1], figsize=(16,8))
sept.set_title("September")


# Analyzing Monthly Rides

# In[33]:


#which is the month with maximum rides
maxrides = df.groupby("month")["hour"].count()
maxridesplot = maxrides.plot.bar(figsize=(16,8))
maxridesplot.set_xlabel("Months")
maxridesplot.set_ylabel("Total number of rides")
maxridesplot.set_title("Rides per month")


# In[34]:


#which is the day with maximum rides
maxdayrides = df.groupby("day")["hour"].count()
maxdayridesplot = maxdayrides.plot.bar(figsize=(16,12))
maxdayridesplot.set_xlabel("Days")
maxdayridesplot.set_ylabel("Total number of rides")
maxdayridesplot.set_title("Rides per day")


# Analyzing demand of uber rides

# In[35]:


#analyzing total rides month wise
dfaprilride = dfapril.groupby("day")["hour"].count()
dfmayride = dfmay.groupby("day")["hour"].count()
dfjuneride = dfjune.groupby("day")["hour"].count()
dfjulyride = dfjuly.groupby("day")["hour"].count()
dfaugustride = dfaugust.groupby("day")["hour"].count()
dfseptride = dfsept.groupby("day")["hour"].count()

fig, ax = plt.subplots(3,2)
aprilrides = dfaprilride.plot.bar(ax=ax[0,0], figsize=(16,8))
aprilrides.set_title("April")

mayrides = dfmayride.plot.bar(ax=ax[0,1], figsize=(16,8))
mayrides.set_title("May")

junerides = dfjuneride.plot.bar(ax=ax[1,0], figsize=(16,8))
junerides.set_title("June")

julyrides = dfjulyride.plot.bar(ax=ax[1,1], figsize=(16,8))
julyrides.set_title("July")

augustrides = dfaugustride.plot.bar(ax=ax[2,0], figsize=(16,8))
augustrides.set_title("August")

septrides = dfseptride.plot.bar(ax=ax[2,1], figsize=(16,8))
septrides.set_title("September")


# In[36]:


#analyzing rush
ax = sns.pointplot(x="hour", y="Lat", hue="weekday", data=df, figsize=(16,8))
ax.set_title("Rush on a particular hour in a day")


# Performing Cross Analysis

# In[37]:


#analyzing which is the most popular base number
basedf = df.groupby(["Base", "month"])["Date/Time"].count().reset_index()
basedf


# In[38]:


pltbase = sns.lineplot(x="month", y="Date/Time", hue="Base", data=basedf)
pltbase.set_xlabel("Month")
pltbase.set_ylabel("Number of Rides")


# In[39]:


#performing cross analysis
def count_rows(rows):
    return len(rows)
def find_cross(a,b,df):
    bycross = df.groupby([a,b]).apply(count_rows)
    pivot = bycross.unstack()
    return sns.heatmap(pivot)
find_cross("weekday", "hour", df)


# In[40]:


find_cross("day", "hour", df)


# In[41]:


find_cross("month", "day", df)


# In[42]:


find_cross("month", "weekday", df)


# Performing Spatial Analysis

# In[54]:


#Analyzing latitudes and longitudes
plt.figure(figsize=(16,8))
plt.scatter(df["Lon"], df["Lat"], c="red", s=0.05, linewidth=0.25)
plt.rcParams['agg.path.chunksize'] = 100000


# In[55]:


#using spatial analysis
df_out = df[df["weekday"]=="Sunday"]
df_out.head()


# In[98]:


rush = df_out.groupby(["Lat", "Lon"])["month"].count().reset_index()
rush.columns=["Lat", "Lon", "no of trips"]
rush


# In[99]:


from folium.plugins import HeatMap
import folium


# In[100]:


basemap=folium.Map()
HeatMap(rush).add_to(basemap)
basemap


# Analyzing Uber Pickups in each month

# In[71]:


uber_15 = pd.read_csv("uber-raw-data-janjune-15.csv")


# In[72]:


uber_15.head()


# In[76]:


uber_15.dtypes


# In[79]:


uber_15["Pickup_date"] = pd.to_datetime(uber_15["Pickup_date"])
uber_15["weekday"] = uber_15["Pickup_date"].dt.day_name()
uber_15["day"] = uber_15["Pickup_date"].dt.day
uber_15["month"] = uber_15["Pickup_date"].dt.month
uber_15["hour"] = uber_15["Pickup_date"].dt.hour
uber_15["minute"] = uber_15["Pickup_date"].dt.minute
uber_15


# In[87]:


ubermonth = uber_15["month"].value_counts()
ubermonth.plot.bar()


# Analyzing Rush in NewYork City

# In[89]:


sns.countplot(uber_15["hour"])


# In[92]:


uberrides = uber_15.groupby(["weekday", 'hour'])["Pickup_date"].count().reset_index()


# In[93]:


uberrides.columns = ["weekday", "hour", "No. of uber rides"]
uberrides


# In[97]:


plt.figure(figsize=(16,8))
sns.pointplot(x="hour", y="No. of uber rides", hue="weekday", data=uberrides)


# Performing indepth analysis of base number

# In[102]:


uber_foil = pd.read_csv("uber-Jan-Feb-FOIL.csv")
uber_foil.head()


# In[105]:


uber_foil["dispatching_base_number"].value_counts()


# In[117]:


#which base number has most active vehicles
sns.boxplot(x="dispatching_base_number",y="active_vehicles",data=uber_foil)


# In[118]:


#which base number has most trips
sns.boxplot(x="dispatching_base_number",y="trips",data=uber_foil)


# In[119]:


uber_foil["Average trips per vehicle"] = uber_foil["trips"]/uber_foil["active_vehicles"]


# In[120]:


uber_foil


# In[131]:


plt.figure(figsize=(16,8))
sns.lineplot(x="date", y="Average trips per vehicle", hue="dispatching_base_number", data=uber_foil)
plt.title("Demand vs Supply Chart")

