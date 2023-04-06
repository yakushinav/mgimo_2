from joblib import dump, load
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
        self.model = load(self.model_file)
        view=VIEW(self.csv_data)
        X=view.get_user_data()
        x = pd.DataFrame(columns=X.keys())
        x.loc[0]=X.values()
        k=view.get_objects_number()
        y = self.model.kneighbors(x, return_distance=False, n_neighbors=k)
        view.print_recomendation(y[0])


