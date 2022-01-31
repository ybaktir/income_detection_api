from sklearn.model_selection import RandomizedSearchCV
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_validate
import pandas as pd
from helper import Imputer, Binarizer, download_census_data
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

download_census_data()

names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
         'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

data = pd.read_csv('data/adult.data', names=names)

model_cols = ['age', 'workclass', 'education', 'education_num', 'marital_status', 'occupation',
              'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country']
cat_cols = ['workclass', 'education', 'marital_status',
            'occupation', 'relationship', 'race', 'sex', 'native_country']
data[cat_cols] = data[cat_cols].apply(lambda x: x.str.lstrip())

y = data.pop('income')


#Spot Check 5 Algorithms (LR, LDA, KNN, CART, GNB, SVM)
models = {'LR': LogisticRegression(),
          'LDA': LinearDiscriminantAnalysis(),
          'KNN': KNeighborsClassifier(),
          'CART': DecisionTreeClassifier(),
          'NB': GaussianNB(),
          'RF': RandomForestClassifier()}

results = []
for name, model in models.items():
    pipe = Pipeline([
        ('imputer', Imputer(['workclass', 'native_country', 'occupation'])),
        ('encoder',  Binarizer(cat_cols)),
        ('classifier', model)
        ])
    cv = cross_validate(pipe, data[model_cols], y, cv=5, n_jobs=-1, scoring='accuracy')
    results.append((name, cv['test_score'].mean()))

print(sorted(results, key=lambda x: x[1], reverse=True))

pipe = Pipeline([
    ('imputer', Imputer(['workclass', 'native_country', 'occupation'])),
    ('encoder',  Binarizer(cat_cols)),
    ('classifier', models['KNN'])
    ])
# pipe.get_params()
param_grid = dict(classifier__leaf_size=list(range(1, 50)),
                  classifier__n_neighbors=list(range(1, 30)), classifier__p=[1, 2])
search = RandomizedSearchCV(pipe, param_grid, n_jobs=-1, random_state=0).fit(data[model_cols], y)
2 ** 13
search.best_params_

# Tune Random Forest
n_estimators = np.array([50, 100, 150, 200, 250])
max_features = np.array([1, 2, 3, 4, 5])
param_grid = dict(n_estimators=n_estimators, max_features=max_features)
model = RandomForestClassifier()
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(X_train, Y_train)
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
'''
# construct the pipeline


cv = cross_validate(model, data[model_cols], y, cv=5)


# fit the pipeline
model.predict(data[model_cols])
model.fit(data[model_cols], y)

model.model_cols = model_cols
model.data_cols = names

#
pickle.dump(model, open('../app/sklearn_income_classifier.pkl', 'wb'))
