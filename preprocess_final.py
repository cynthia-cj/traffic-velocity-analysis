import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta

#read csv file of dataset
df= pd.read_csv("yellow_tripdata_2019-01.csv", usecols=["tpep_pickup_datetime","tpep_dropoff_datetime","trip_distance","PULocationID","DOLocationID"])
#df=df1.head(20)
neighbor=pd.read_csv("C&N-MANHATTAN_updated.csv")
objID=neighbor['Region ID'].tolist()
'''
new=df["tpep_pickup_datetime"].str.split(" ", n=1,expand= True)
df["pickup_Date"] = new[0]
df["pickup_Time"]=new[1]
df.drop(columns=["tpep_pickup_datetime"], inplace= True)

#print(df)

new1= df["tpep_dropoff_datetime"].str.split(" ", n=1,expand= True)
df["dropoff_Date"] = new1[0]
df["dropoff_Time"]=new1[1]
df.drop(columns=["tpep_dropoff_datetime"], inplace= True)
'''
#change the date column values from string to date format
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
#df["pickup_Time"] = pd.to_datetime(df["pickup_Time"])
#df["dropoff_Time"]=pd.to_datetime(df["dropoff_Time"])

#removing taxi records that are not in 2019
df= df[(df['tpep_pickup_datetime'] > "2018-12-31") & (df['tpep_pickup_datetime'] < "2020-01-01")]
df= df[(df['tpep_dropoff_datetime'] > "2018-12-31") & (df['tpep_dropoff_datetime'] < "2020-01-01")]


#removing records for whilch trip distance is less than 1 mile
df.drop(df.index[df['trip_distance'] < 1], inplace=True)

#removing records for which pickup or dropoff was not in New York
df.drop(df.index[df['PULocationID'] >263],inplace=True)
df.drop(df.index[df['DOLocationID'] >263],inplace=True)

df=df[df['PULocationID'].isin(objID)]
df=df[df['DOLocationID'].isin(objID)]


df["time_taken_secs"]=df.tpep_dropoff_datetime - df.tpep_pickup_datetime
df["time_taken_secs"]=df.time_taken_secs / np.timedelta64(1,'s')
df["velocity (km/h)"]=(df.trip_distance / df.time_taken_secs)*60*60
df["velocity (km/h)"]=(df["velocity (km/h)"]) * 1.60934

print(df)
df.to_csv('yellow_clean_final.csv')

#divide tempeorally





#for i in range(len(df)):
 #   x=[]
  #  x=df['trip_distance'].tolist()
#print(x)

