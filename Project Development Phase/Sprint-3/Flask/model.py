import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
import joblib


df = pd.read_csv('general_data.csv')

df.drop(['EmployeeID','EmployeeCount','Over18','StockOptionLevel'],axis=1,inplace=True)

df.drop_duplicates(inplace=True)

X = df.drop('Attrition', inplace=False, axis=1)
y = df.Attrition

ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')

ct = make_column_transformer((ohe, make_column_selector(dtype_include='object')),
                            remainder='passthrough')


rnd = RandomForestClassifier(n_estimators=500,min_samples_split=80,min_samples_leaf=2,
                             max_features='log2',max_depth=8,random_state=42)

lgbm = LGBMClassifier(random_state=42)

vc = VotingClassifier(estimators=[('rnd', rnd), ('lgbm', lgbm)],voting='soft', n_jobs=-1)

pipe = make_pipeline(ct,vc)

pipe.fit(X, y)

filename = 'model.pkl'
joblib.dump(pipe, filename)
