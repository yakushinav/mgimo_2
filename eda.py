import pandas as pd
import numpy as np

df=pd.read_csv('Bengaluru_House_Data.csv')

print(df.head())
print(df.info())
print(df.groupby('area_type').size())
#df=df.drop(df[df['area_type'].isna()].index)
df=df.dropna(how='all')

df = df.drop('society',axis=1)

print(df.info())
print(df[df['location'].isna()])

df['location']=df['location'].str.strip()
df['location']=df['location'].str.lower()

#print(df['location'].mode())
df['location']=df['location'].fillna(df['location'].mode()[0])
df['location']=df['location'].str.lstrip('1230456789 ')
print(df[df['location'].str.contains("channasandra")].groupby('location').size())
df.loc[df['location'].str.contains("channasandra"),'location']="channasandra"
df.loc[df['location'].str.contains("yeshwanthpur"),'location']="yeshwanthpur"
df.loc[df['location'].str.contains("yemlur"),'location']="yemlur"
#print(df[df['location'].str.contains("channasandra")].groupby('location').size())
print(df.groupby('location').size())
print(df[df['location'].str.contains("yelahanka")].groupby('location').size())
print(df.info())