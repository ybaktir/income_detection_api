from sklearn.metrics import classification_report
from helper import download_census_data
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
import numpy as np

download_census_data()

names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
         'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

data = pd.read_csv('data/adult.data', names=names)
cat_cols = ['workclass', 'education', 'marital_status',
            'occupation', 'relationship', 'race', 'sex', 'native_country']

# cleaning the blank character at the beginning of the strings
data[cat_cols] = data[cat_cols].apply(lambda x: x.str.lstrip())
data[cat_cols] = data[cat_cols].astype(str)


remove_cols = ['fnlwgt']
target_col = ['income']

model_cols = [col for col in data.columns if col not in remove_cols + target_col]

y = data.pop('income')


X_train, X_valid, y_train, y_valid = train_test_split(data[model_cols], y, random_state=1, test_size=.2)

cat_cols = ['workclass', 'education', 'marital_status',
            'occupation', 'relationship', 'race', 'sex', 'native_country']
cat_features = [i for i, v in enumerate(X_train.columns) if v in cat_cols]


model = CatBoostClassifier(iterations=1000,
                           learning_rate=0.1,
                           loss_function='Logloss',
                           custom_metric='Accuracy',
                           l2_leaf_reg=2,
                           random_strength=5,
                           # depth=8
                           )
model.fit(X_train,
          y_train,
          cat_features=cat_features,
          eval_set=(X_valid, y_valid),
          early_stopping_rounds=100,
          use_best_model=True,
          verbose=True)

model.model_cols = model_cols
model.data_cols = names


model.save_model("../app/catboost_income_classifier.cbm")
#
