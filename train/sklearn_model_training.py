import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_validate
import pandas as pd
from helper import Imputer, Encoder, download_census_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

download_census_data()

names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
         'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

data = pd.read_csv('data/adult.data', names=names)


data['income'] = data['income'].replace({' <=50K': 0, ' >50K': 1})

model_cols = ['age', 'workclass', 'education', 'education_num', 'marital_status', 'occupation',
              'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country']
cat_cols = ['workclass', 'education', 'marital_status',
            'occupation', 'relationship', 'race', 'sex', 'native_country']

y = data.pop('income')


# construct the pipeline
model = Pipeline([
    ('imputer', Imputer(['workclass', 'native_country', 'occupation'])),
    ('encoder',  Encoder(cat_cols)),
    ('classifier', RandomForestClassifier())
    ])


# fit the pipeline
model.fit(data[model_cols], y)

model.model_cols = model_cols
model.data_cols = names

#
pickle.dump(model, open('../app/sklearn_income_classifier.pkl', 'wb'))
