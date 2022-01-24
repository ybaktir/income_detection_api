import requests
import json

url = "http://127.0.0.1:8080/predict"
url = "http://127.0.0.1:6660/predict"


payload = json.dumps(
            {'age': 25,
             'workclass': 'Private',
             'education': '11th',
             'education_num': 7,
             'marital_status': 'Never-married',
             'occupation': 'Machine-op-inspct',
             'relationship': 'Own-child',
             'race': 'Black',
             'sex': 'Male',
             'capital_gain': 0,
             'capital_loss': 0,
             'hours_per_week': 40,
             'native_country': 'United-States'}
)


headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST",
                            url,
                            headers=headers,
                            data=payload)

response.text
