import numpy as np
import pandas as pd

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, cophenet
from scipy.spatial.distance import cdist, pdist

from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt
import seaborn as sns


import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import StandardScaler
from pathlib import Path

import pca
import knn
import dendrogram
import importance_by_class
import decision_tree_maker
import parse_dot_file


def remove_extra_values(dataframe):
    zero_class_count, first_class_count = 0, 0
    zero_class_limit, first_class_limit = 20000, 492
    new_dataframe = pd.DataFrame(columns=dataframe.columns)
    for index, row in dataframe.iterrows():
        if row["Class"] == 0 and zero_class_count < zero_class_limit:
            new_dataframe = new_dataframe.append(row)
            zero_class_count += 1
        if row["Class"] == 1 and first_class_count < first_class_limit:
            new_dataframe = new_dataframe.append(row)
            first_class_count += 1
        if zero_class_count == zero_class_limit and first_class_count == first_class_limit:
            return new_dataframe


def encoding_categorical_variables(df: pd.DataFrame, names):
    res = pd.get_dummies(df, columns=names, prefix=names)
    return res


if __name__ == '__main__':
    # dataframe = pd.read_csv("three_dim.csv")
    # dataframe.to_excel("creditcard_edited.xlsx")

    # three_dimensional_data = pca.get_3_dimensional_data(dataframe)
    # three_dimensional_data.to_excel("three_dimensional.xlsx")

    # df = pd.read_csv('application_data.csv')
    # df.to_excel('application_data.xlsx')
    dataframe = pd.read_csv("heart.csv")
    dataframe = encoding_categorical_variables(dataframe, ['Sex', 'ChestPainType', 'FastingBS', 'RestingECG',
                                                     'ExerciseAngina', 'ST_Slope'])
    # three_dimensional_data = pd.read_csv("three_dim.csv")
    # features_df, ff = importance_by_class.importance_by_class(dataframe)
    # importance_by_class.plot_features_by_class(features_df, ff)
    x_train, x_test, y_train, y_test = knn.get_test_train_data(dataframe)
    #
    decision_tree_maker.create_decision_tree(x_train, x_test, y_train, y_test)
    decision_tree_maker.create_decision_tree(dataframe.drop(columns=['Class']), x_test, dataframe['Class'], y_test)
    #
    # class_0, class_1 = dataframe[dataframe['Class'] == 0], dataframe[dataframe['Class'] == 1]
    # pca.visualise(dataframe.drop(columns=['Class']), x_test, dataframe['Class'], y_test)
    # pca.visualise(x_train, x_test, y_train, y_test)

    # main_components = dataframe[["V4", "V14", "V21", "V26", "Amount", "Class"]]
    # principal_components, weights, weights_t_classes = pca.get_components_weights(dataframe)
    # principal_components.to_csv('three_dim.csv', index=False)
    # x_train, x_test, y_train, y_test = knn.get_test_train_data(dataframe)
    # cm, f1_score,  accuracy_score, output_df = knn.calculate_knn(x_train, x_test, y_train, y_test)
    # pca.plot_3d(output_df)
    # pca.visualise_weights(weights, 3, ['Component 1', 'Component 2', 'Component 3'])

    # features_indices_by_component = pca.get_significant_features_by_component(weights_t_classes)
    # component_significance_by_class = pca.get_component_weight_by_class(features_indices_by_component,
    #                                                                     weights_t_classes)
    # dendrogram.plot_dendrogram(three_dimensional_data)


    # Time, V14, V4

    v = 1
