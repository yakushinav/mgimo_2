import pandas as pd
import numpy as np

# Визуализация данных
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('Bengaluru_House_Data.csv')

#print(df.head())
#print(df.info())
#print(df.groupby('area_type').size())
#df=df.drop(df[df['area_type'].isna()].index)
df=df.dropna(how='all')

df = df.drop('society',axis=1)

#print(df.info())
#print(df[df['location'].isna()])

df['location']=df['location'].str.strip()
df['location']=df['location'].str.lower()

#print(df['location'].mode())
df['location']=df['location'].fillna(df['location'].mode()[0])
df['location']=df['location'].str.lstrip('1230456789 ')
#print(df[df['location'].str.contains("channasandra")].groupby('location').size())
df.loc[df['location'].str.contains("channasandra"),'location']="channasandra"
df.loc[df['location'].str.contains("yeshwanthpur"),'location']="yeshwanthpur"
df.loc[df['location'].str.contains("yemlur"),'location']="yemlur"
#print(df[df['location'].str.contains("channasandra")].groupby('location').size())
#print(df.groupby('location').size())
#print(df[df['location'].str.contains("yelahanka")].groupby('location').size())
#print(df.info())
#print(df.groupby('size').size())
df['size']=df['size'].str.split(' ',expand=True)[0].astype(np.number)
#print(df.groupby('balcony').size())
#print(df[df['balcony'].isna()])
df['balcony']=df['balcony'].fillna(0)
df['bath']=df['bath'].fillna(0)
#print(df.groupby('bath').size())
df=df.dropna(subset=['size'])
#df=df.dropna()
#print(df.info())
#print(df[df['size'].isna()])
#print(df.head())
#print(df.groupby('availability').size())
#print(df.availability=='Ready To Move')
df.availability=df.availability=='Ready To Move'
df.availability.replace({True:1,False:0},inplace=True)
df.availability=df.availability.astype('category')

df['area_type']=df['area_type'].astype('category')
#df1=pd.get_dummies(df['area_type'])
#df=pd.concat([df,df1],axis='columns')
print(df.head())
#rp={'Built-up  Area':0,'Carpet  Area':1,'Plot  Area':2,'Super built-up  Area':3}
#df.area_type.replace(rp,inplace=True)

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['area_type']=label_encoder.fit_transform(df['area_type'])
df['location']=label_encoder.fit_transform(df['location'])
df['area_type']=df['area_type'].astype('category')
df['location']=df['location'].astype('category')

#print(df.groupby('area_type').size())
print(df.describe())
'''
scaler=preprocessing.MinMaxScaler()
df_numeric=df.select_dtypes(np.number)
df_cat=df.select_dtypes(exclude=np.number)
df_cat=df_cat.reset_index()
print(df_numeric.head())
df_numeric_scaled=pd.DataFrame(scaler.fit_transform(df_numeric,df_numeric),columns=df_numeric.columns)
print(df_numeric_scaled.head())
print(df_cat.head())
'''
df.to_csv('Bangalor_clean.csv')
df.plot(kind='scatter',x='size', y='price')
plt.show()
