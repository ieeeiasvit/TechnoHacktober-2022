#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


# In[2]:


#Loading Dataset
dataset = pd.read_csv("C:\\Users\\Harsha\\Desktop\\Machine Learning\\20BCE0295\\processed.cleveland.data.csv", names=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'output'])
dataset_mean = dataset


# In[3]:


#Data Preprocessing

#Filling missing values Statistics measures
print("*****Before Filling Missing values Row 166, 192, 287, 302*****")
print(dataset_mean.loc[287])
dataset1 = dataset_mean
df1 = pd.DataFrame(dataset1)

print("----- Mean of Column 11 'ca' -----")
print(df1['ca'].mean())
df1.fillna(df1.mean(), inplace=True)
print("*****After Filling Missing values Row 166, 192, 287, 302*****")
print(df1.loc[[166, 192, 287, 302]])

print("----- Mean of Column 12 'thal' -----")
print(df1['thal'].mean())
df1.fillna(df1.mean(), inplace=True)
print("*****After Filling Missing values Row 87, 266*****")
print(df1.loc[[87, 266]])


# In[4]:


#Dataset Description

#Number of patients
n_patients = dataset.shape[0]

#Number of features
n_features = dataset.shape[1]-1

dataset["output"].replace(to_replace=[1, 2, 3, 4], value=1, inplace=True)

#With Heart Disease
heart_disease = dataset[dataset['output'] == 1].shape[0]

#Without Heart Disease
no_heart_disease = dataset[dataset['output'] == 0].shape[0]

#Printing Results
print("Total number of patients: {}".format(n_patients))
print("Number of features: {}".format(n_features))
print("Number of patients with Heart Disease: {}".format(heart_disease))
print("Number of patients without Heart Disease: {}".format(no_heart_disease))


# In[5]:


#Extracting feature columns
feature_cols = list(dataset.columns[0:13])

#Showing the list of columns
print("Feature columns: \n{}".format(feature_cols))


# In[6]:


#Separate the data into feature data and target data (X_all and y_all, respectively)
X = dataset[feature_cols]
y = dataset['output'].values

#Showing the feature information by printing the first five rows
print("\nFeature values:")
X.head()


# In[7]:


#Splitting the Dataset into Training and Testing data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)
print(X_train)


# In[8]:


#RandomForest Classifier

print("RandomForest Classifier")

model = RandomForestClassifier(n_estimators = 50, random_state = 1)
model.fit(X_train, y_train)
y_predictions = model.predict(X_test)

cm1 = confusion_matrix(y_test, y_predictions)
print("Accuracy =", accuracy_score(y_predictions, y_test))


# In[9]:


#AdaBoost Classifier

print("AdaBoost Classifier")

model = AdaBoostClassifier(n_estimators = 50)
model.fit(X_train, y_train)
y_predictions = model.predict(X_test)

cm1 = confusion_matrix(y_test, y_predictions)
print("Accuracy =", accuracy_score(y_predictions, y_test))

