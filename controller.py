from joblib import load
import pandas as pd
from view import VIEW
from model import ML_MODEL

class BOT():
    def __init__(self,filename):
        self.csv_data=filename
        self.clean_data=""
        self.model_file='model.dump'


    def create_model(self):
        dm = ML_MODEL(self.csv_data)
        self.clean_data=dm.get_clean_data()
        dm.build_model()

    def get_recommentation(self):
        #Загружаем скомпилированную модель
        self.model = load(self.model_file)
        #Создаем экземпляр view на основе очищенного набора данных
        view=VIEW(self.clean_data)
        # Читаем ввод пользователя
        X=view.get_user_data()
        # Создаем набор данных для построения рекомендации
        x = pd.DataFrame(columns=X.keys())
        x.loc[0]=X.values()
        # Вводим количество объектов в рекомендации
        k=view.get_objects_number()
        # Строим рекомендацию
        y = self.model.kneighbors(x, return_distance=False, n_neighbors=k)
        # Выводим найденные объекты на экран
        view.print_recomendation(y[0])


