from sklearn.metrics import classification_report
from catboost import CatBoostClassifier
import pandas as pd
import pickle

model = pickle.load(open('../app/sklearn_income_classifier.pkl', 'rb'))
model_cols = model.model_cols
names = model.data_cols

test = pd.read_csv('data/adult.test', skiprows=1, names=names)

y_test = test.pop('income').str.replace('\.', '', regex=True)
y_test_dummy = y_test.replace({' <=50K': 0, ' >50K': 1})

sklearn_income_classifier = pickle.load(open('../app/sklearn_income_classifier.pkl', 'rb'))
y_pred_sklearn = sklearn_income_classifier.predict(test[model_cols])


print(classification_report(y_test_dummy, y_pred_sklearn))

catboost_income_classifier = CatBoostClassifier()
catboost_income_classifier.load_model('../app/catboost_income_classifier.cbm')
y_pred_catboost = catboost_income_classifier.predict(test[model_cols])
print(classification_report(y_test, y_pred_catboost))
