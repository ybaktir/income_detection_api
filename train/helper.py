from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import warnings
warnings.filterwarnings("ignore")


def download_census_data(path='data'):
    urls = (
        "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
        "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names",
        "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test",
    )
    if not os.path.exists(path):
        os.mkdir(path)

    for url in urls:
        response = requests.get(url)
        name = os.path.basename(url)
        with open(os.path.join(path, name), 'wb') as f:
            f.write(response.content)


class Imputer(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        self.columns = columns
        self.imputer = None

    def fit(self, data, target=None):

        self.imputer = SimpleImputer(missing_values='?', strategy='most_frequent')
        self.imputer.fit(data[self.columns])

        return self

    def transform(self, data):

        output = data.copy()
        output[self.columns] = self.imputer.transform(output[self.columns])

        return output


class Encoder(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        self.columns = columns
        self.encoders = None

    def fit(self, data, target=None):

        self.encoders = {
            column: LabelEncoder().fit(data[column])
            for column in self.columns
        }
        return self

    def transform(self, data):

        output = data.copy()
        for column, encoder in self.encoders.items():
            output[column] = encoder.transform(data[column])

        return output


class Plotter:

    def __init__(self, data):
        """Constructor for the Plotter Class"""
        self.data = data

    def plot_hist_per_target(self, target, histtype='bar', bins=30, overlay=True):
        """Plot all variables"""

        for col in self.data.columns.tolist():
            if col in target:
                continue
            plt.rcParams['figure.figsize'] = (10, 5)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            if overlay and is_numeric_dtype(self.data[col]):
                self.data.groupby(target)[col].plot(kind='hist', bins=30,
                                                    histtype=histtype, ax=ax, legend=True)
            else:
                self.data[col].hist(by=self.data[target], bins=30, histtype=histtype, ax=ax)
            ax.set_xlabel('distribution of {}'.format(col))
            ax.set_ylabel('event counts')
            plt.show()

    def plot_cor(self, variable_list, z_min=-1, z_max=1, round=2):
        """Plot correltation matrix"""
        cor_df = self.data[variable_list]
        cor_df = cor_df.corr().round(round)

        plt.rcParams['figure.figsize'] = (8, 8)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        s = sns.heatmap(cor_df, annot=True, fmt="g", vmin=z_min, vmax=z_max, ax=ax)

    def plot_countplot(self, x, hue, data):
        plt.figure(figsize=(10, 5))
        sns.countplot(x=x, hue=hue, data=data)
        plt.xticks(rotation=90)

    def plot_barplot(self, x, y):
        plt.figure(figsize=(10, 5))
        sns.barplot(palette='deep', x=x, y=y, data=self.data[y].value_counts().reset_index())
        plt.xticks(rotation=90)

    def plot_scatter_per_target(self, target, histtype='scatter'):
        """Plot all variables"""
        data_ = self.data._get_numeric_data()
        for col in list(data_):
            if col in target:
                continue
            plt.rcParams['figure.figsize'] = (10, 5)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            self.data.plot(kind='scatter', x=col, y=target, ax=ax, legend=True)
            ax.set_xlabel('{}'.format(col))
            ax.set_ylabel('{}'.format(target))
            plt.show()
