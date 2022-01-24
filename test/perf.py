import json
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def testFastAPI(self):
        load = {'age': 25,
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
        myheaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.client.post("/predict", data=json.dumps(load), headers=myheaders)
