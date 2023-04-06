import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load

class ML_MODEL():
    def __init__(self,filename):
        self.filename=filename
        # Читаем набор данных
        self.df = pd.read_csv(filename)

    def get_clean_data(self):
        # Данное поле содержит очень много пропусков, удаляем
        self.df.drop('society',axis=1,inplace=True)
        # Заменяем пропуски в данных
        self.df.location.replace(to_replace=np.NaN,value=self.df.location.mode()[0],inplace=True)
        self.df.area_type.replace(to_replace=np.NaN,value=self.df.area_type.mode()[0],inplace=True)
        self.df['size']=self.df['size'].str.split(' ',expand=True)[0].astype(np.number)
        self.df['size'] = self.df['size'].fillna(1)
        self.df.bath=self.df.bath.astype(np.number)
        self.df['bath'] = self.df['bath'].fillna(1)
        self.df.balcony = self.df.balcony.astype(np.number)
        self.df['balcony'] = self.df['balcony'].fillna(0)
        self.df.availability=(self.df.availability=='Ready To Move')
        self.df.availability.replace({True:1,False:0},inplace=True)
        self.df['availability'] = self.df['availability'].astype(np.number)

        #Заменяем пропуски в данных на основе интерполяции
        self.df['total_sqft'] = self.df['total_sqft'].interpolate(method='polynomial', order=2)
        self.df['price'] = self.df['price'].interpolate(method='polynomial', order=2)
        # на этом шаге сохраним набор очищенный набор данных
        self.df.to_csv(self.filename.split(".")[0] + "_clean.csv")
        # Далее заменяем категориальные данные на числовые коды
        encoder = LabelEncoder()
        self.df['area_type'] = encoder.fit_transform(self.df['area_type'])
        self.df['area_type']=self.df['area_type'].astype(np.number)
        self.df['location'] = encoder.fit_transform(self.df['location'])
        self.df['location'] = self.df['location'].astype(np.number)
        return self.filename.split(".")[0] + "_clean.csv"

    def build_model(self):
        self.model = NearestNeighbors(metric='cosine')
        self.model.fit(self.df)
        dump(self.model,"model.dump")


