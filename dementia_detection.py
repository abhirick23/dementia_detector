# -*- coding: utf-8 -*-
"""dementia_detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aomojQH4nqyzUyxagvpdmrndHZvyHJec
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
import joblib

"""# Uploading Dataset"""

df_train=pd.read_csv(r'E:\django_projects\dementia_detector\dementia_dataset.csv')
df_train.head()

df_train.info()

df_train.describe().style.background_gradient(axis=0,cmap = 'RdYlGn')

"""# EDA"""

df_train.isna().sum()

df_train['SES']=df_train['SES'].fillna(df_train['SES'].mean())
df_train['MMSE']=df_train['MMSE'].fillna(df_train['MMSE'].mean())

df_train.columns

df_train.Group.value_counts()

columns = df_train.columns
binary_cols = []
remain_cols=[]
for col in columns:
    if df_train[col].value_counts().shape[0] == 2:
        binary_cols.append(col)
    else:
      remain_cols.append(col)

binary_cols

sns.countplot("Group", data=df_train)

sns.countplot("Visit", data=df_train)

sns.countplot("M/F", data=df_train)

Group_numeric = {'Nondemented':2, 'Demented':1,'Converted':0}
df_train.Group.replace(Group_numeric, inplace=True)

plt.figure(figsize=(12,9),dpi = 100)
sns.heatmap(df_train.corr(),vmax=.8,annot = True, square = True)
plt.show()

fig, ax = plt.subplots(4, 2, figsize = (15, 13))
sns.boxplot(x= df_train["ASF"], ax = ax[0,0])
sns.distplot(df_train['ASF'], ax = ax[0,1])
sns.boxplot(x= df_train["nWBV"], ax = ax[1,0])
sns.distplot(df_train['nWBV'], ax = ax[1,1])
sns.boxplot(x= df_train["eTIV"], ax = ax[2,0])
sns.distplot(df_train['eTIV'], ax = ax[2,1])
sns.boxplot(x= df_train["CDR"], ax = ax[3,0])
sns.distplot(df_train['CDR'], ax = ax[3,1])
plt.tight_layout()

sns.set(rc={'figure.figsize':(11.7,8.27)})
cData_attr = df_train.iloc[:, 0:7]
sns.pairplot(cData_attr, diag_kind='kde')

X = df_train.drop(['Subject ID', 'MRI ID', 'M/F', 'Hand','Group'], axis = 1)
Y = df_train["Group"]
x_Data = X.values
y_Data = Y.values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_Data, y_Data, test_size = 0.2, random_state = 42)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix



"""# Random forest Classifier"""

from sklearn.ensemble import RandomForestClassifier as rf

clf_forest = rf(n_estimators=100, max_depth=10)
clf_forest.fit(X_train, y_train)

pred = clf_forest.predict(X_train)
accuracy_score(y_train, pred)

confusion_matrix(y_train, pred)

pred_test = clf_forest.predict(X_test)
accuracy_score(y_test, pred_test)




"""# Model saving"""

filename1 = 'random_forest_Classifier.sav'
joblib.dump(clf_forest, filename1)