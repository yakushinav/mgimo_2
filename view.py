import pandas as pd
import difflib


class VIEW():
    def __init__(self,filename):
        self.df=pd.read_csv(filename)

    def get_simp(self,s, lst):
        #Выбирает название из списка максимально похожее на ввод пользователя
        normalized1 = s.lower()
        mratio=0
        simp=0
        for k in range(len(lst)):
            normalized2 = lst[k].lower()
            matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
            r= matcher.ratio()
            if r>mratio:
                mratio=r
                simp=k
        return simp

    def get_user_data(self):
        X = {'area_type': 0,
             'availability': 1,
             'location': 300,
             'size': 2,
             'total_sqft': 300,
             'bath': 1,
             'balcony': 1,
             'price': 300}
        print("Введите данные для подбора объекта недвижимости:")
        print('Тип объекта недвижимости')
        lst=self.df['area_type'].unique()
        #print('У нас в базе есть следующие типы:\n',", ".join(lst))
        choose=input("Введите тип объекта недвижимости: ")
        X['area_type']=self.get_simp(choose,lst)
        return X

    def get_objects_number(self):
        choose=int(input('Введите количество объектов в рекомендации: '))
        return choose

    def print_recomendation(self,lst):
        print('Вашему запросу соответствуют следующие объекты недвижимости:')
        for x in lst:
            print("---------",x,"------------")
            print(self.df.loc[x])



