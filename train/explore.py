from helper import Plotter
import pandas as pd

names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
         'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
data = pd.read_csv('data/adult.data', names=names)
data.drop('fnlwgt', axis=1, inplace=True)

data['income'] = data['income'].replace({' <=50K': 0, ' >50K': 1})

plot = Plotter(data)
plot.plot_hist_per_target('income')
plot.plot_cor(['age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week', 'income'])
plot.plot_scatter_per_target('income')


data['workclass'].hist(by=data['income'])
