from person import Person
import sys
from fastapi import FastAPI
from catboost import CatBoostClassifier
import uvicorn
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
sys.path.append(dir_path)


app = FastAPI()
model = CatBoostClassifier()
model.load_model('catboost_income_classifier.cbm')


@app.get('/')
def index():
    return {'message': 'This is the homepage of the API '}


@app.post('/predict')
def get_person(data: Person):
    received = data.dict()
    age = received['age']
    workclass = received['workclass']
    education = received['education']
    education_num = received['education_num']
    marital_status = received['marital_status']
    occupation = received['occupation']
    relationship = received['relationship']
    race = received['race']
    sex = received['sex']
    capital_gain = received['capital_gain']
    capital_loss = received['capital_loss']
    hours_per_week = received['hours_per_week']
    native_country = received['native_country']
    pred_name = model.predict([age,
                               workclass,
                               education,
                               education_num,
                               marital_status,
                               occupation,
                               relationship,
                               race,
                               sex,
                               capital_gain,
                               capital_loss,
                               hours_per_week,
                               native_country])
    return {'prediction': pred_name}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80, debug=True)
